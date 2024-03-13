from .OOInterface import *
from .Node import *
from .Element import *
from typing import TextIO

class Mesh(OOInterface):  
  """Class Mesh used to store node and element information of a FE mesh
  """
#   ****************** 
#      INITIALIZER
#   ******************
  def __init__(self, dim: int):
    """Default Initializer. nodes and elements should be added with the provided methods

    Args:
        dim (int): dimension of the mesh (1, 2 or 3)
    """
    if dim < 1 or dim > 3:
      DebugStop(f"Mesh dimension *{dim}* not supported")
    
    super().__init__()
    self.dim = dim
    self.nodevec: list[Node] = []
    self.elvec: list[Element] = []    
    super().activateChecks()

#   ****************** 
#        METHODS
#   ******************   
  def nnodes(self)->int:
    """Returns number of nodes in the mesh"""
    DebugStop("YOUR CODE GOES HERE")

# ------------------------------------------------
# ------------------------------------------------

  def nel(self)->int:
    """Returns number of elements in the mesh"""
    DebugStop("YOUR CODE GOES HERE")

# ------------------------------------------------
# ------------------------------------------------

  def addNode(self,node: Node):
    """Adds a node to the mesh"""
    self.nodevec.append(node)
    node.index = len(self.nodevec) - 1

# ------------------------------------------------
# ------------------------------------------------

  def addEl(self,el: Element):
    """Adds an element to the mesh"""
    self.elvec.append(el)
    el.index = len(self.elvec) - 1
    el.buildEFT()

# ------------------------------------------------
# ------------------------------------------------

  def nequations(self)->int:
    DebugStop("YOUR CODE GOES HERE")
    # Loop through elements and count the number of state variables
    # Note you will have to avoid counting the same node twice
    # One option is to use a boolean array to keep track of which nodes have been counted
    
    # return neq

# ------------------------------------------------
# ------------------------------------------------

  def generateGeometryVTK(self, filename: str):
    DebugStop("YOUR CODE GOES HERE")

    # 0. Open file to write
    f = open(filename,"w")

    # 1. Print header

    # 2. Print nodes

    # 3. Print element connectivity

    # 4. Print element types
    #  Note you can just use the vtktype method of the element class

    # 5. Print element index as FieldData

    # 6. Close file  
    f.close()

# ------------------------------------------------
# ------------------------------------------------

  # This function is generated for you. It duplicates the nodes of the elements in order to show what happens at interfaces
  def generatePostProcVTK(self, filename: str):
    # 0. Open file
    f = open(filename,"w")
    # 1. Print header
    f.write("# vtk DataFile Version 4.0\n")
    f.write("PyFET Mesh\n")
    f.write("ASCII\n")
    f.write("DATASET UNSTRUCTURED_GRID\n\n")

    # 2. Print nodes (loop through elements and duplicate nodes if necessary)
    ntotalnodes = np.sum([el.nnodes() for el in self.elvec if el.dim == self.dim])
    f.write(f"Points {ntotalnodes} float\n")
    for el in self.elvec:
      if el.dim != self.dim: continue
      for nodind in el.nodeorder():
        nod = el.nodevec[nodind]
        if len(nod.coord) == 2:
          f.write(" ".join(np.append(nod.coord,0.).astype(np.str_)) + "\n")
        else:
          f.write(" ".join(nod.coord.astype(np.str_)) + "\n")

    # 3. Print element connectivity
    ndimels = np.sum([1 for el in self.elvec if el.dim == self.dim])        
    nentries = np.sum([len(el.nodevec)+1 for el in self.elvec if el.dim == self.dim])
    f.write(f"\nCells {ndimels} {nentries}\n")
    nodcounter = 0
    for el in self.elvec:
      if el.dim != self.dim: continue
      elinfo = f"{len(el.nodevec)} "
      for nod in el.nodevec:
        elinfo += f"{nodcounter} "
        nodcounter += 1      
      f.write(elinfo + "\n")

    # 4. Print element types
    f.write(f"\nCell_types {ndimels}\n")
    for el in self.elvec:
      if el.dim != self.dim: continue
      f.write(f"{el.vtktype()}\n")

    # 5. Print element information
    f.write(f"\nCell_data {ndimels}\n")
    f.write(f"Field FieldData 1\n") # Only el index 
    f.write(f"elindex 1 {ndimels} int\n")
    for el in self.elvec:
      if el.dim != self.dim: continue
      f.write(f"{el.index}\n")

    # 6. Close file  
    f.close()

# ------------------------------------------------
# ------------------------------------------------

  def __str__(self) -> str:
    head = "@@@@@@@@@@@ Mesh Information @@@@@@@@@@@"
    nodeinfo = f"\n------- Node info ------\nMesh nodes = {self.nnodes()}\n\n" + "".join([node.__str__() for node in self.nodevec])
    elinfo = f"\n------- Element info ------\nMesh elements = {self.nel()}\n" + "".join([el.__str__() for el in self.elvec])    
    return head + nodeinfo + elinfo

# ------------------------------------------------
# ------------------------------------------------
