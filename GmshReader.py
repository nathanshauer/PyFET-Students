import gmsh
# import numpy as np
import os.path
from .OOInterface import *
from .Mesh import *
from typing import Literal
from .TrussDSMBC import *
from .BarBC import *
from .Bar2Node import *
from .Bar3Node import *
from .ElasTria3 import *
from .ElasQuad4 import *
from .ElasBC import *
from .ElasPtBC import *

class GmshReader(OOInterface):
  """Class used to read a mesh from a Gmsh file
  """
#   ****************** 
#      INITIALIZER
#   ******************
  def __init__(self,physicalgroupToBC: list = [],type: Literal["TrussDSM","Truss","Elas2D","Elas3D"] = "Elas2D"):
    """Initializer for GmshReader class
    Args:
        physicalgroupToBC (list, optional): a dictionary that relates name of physical group used on gmsh with actual BC necessary data. Defaults to [].
        type (Literal[&quot;TrussDSM&quot;,&quot;Truss&quot;,&quot;Elas2D&quot;,&quot;Elas3D&quot;], optional): Type of reader to use. Defaults to "Elas2D".
    """
    super().deactivateChecks()
    self.type = type
    if type == "Bar2Node" or type == "TrussDSM":
      self.domainElDim = 1
    elif type == "Elas2D":
      self.domainElDim = 2
    elif type == "Elas3D":
      self.domainElDim = 3
    else:
      DebugStop(f"GmshReader for simulation type *{type}* not supported")
    self.physicalgroupToBC = physicalgroupToBC
    self._gmshElTypes = {1: "line", 2: "tria", 3: "quad", 4: "tet", 5: "hex", 6: "prism", 7: "pyr", 8: "line3", 9: "tria6", 10: "quad9", 11: "tet10", 12: "hex27",13: "prism18", 14: "pyr14", 15: "node"}
    self._gmeshElTypeToNNodes = {"node": 1, "line": 2, "tria": 3, "quad": 4, "tet": 4, "hex": 8, "prism": 6, "pyr": 5, "line3": 3, "tria6": 6, "quad9": 9, "tet10": 10, "hex27": 27, "prism18": 18, "pyr14": 14}
    self.mesh = None
    gmsh.initialize()
    super().activateChecks()

# ------------------------------------------------
# ------------------------------------------------

  def readMesh(self,filename: str = ""):
    if not os.path.isfile(filename):
      DebugStop(f"File {filename} not found")

    gmsh.open(filename)
        
    dim = -1
    if self.type == "Bar2Node" or self.type == "Bar3Node":
      dim = 1
    elif self.type == "TrussDSM" or self.type == "Elas2D":
      dim = 2
    elif self.type == "Elas3D":
      dim = 3
    else:
      DebugStop(f"Simulation type *{self.type}* not supported")

    self.mesh = Mesh(dim=dim)

    # 1. Adding nodes
    nodes_tags,nodes_coord,bogus = gmsh.model.mesh.getNodes(dim=-1)
    nnodes = len(nodes_tags)
    for inod in range(nnodes):
      nodecoord = nodes_coord[3*inod:3*(inod+1)]
      node = Node(nodecoord)
      self.mesh.addNode(node)
    
    # 2. Adding elements
    # We have to loop over each physical group that has dimension     
    for idim in range(self.domainElDim+1):
      physical_group_tags = gmsh.model.getPhysicalGroups(idim)

      for _, pg_tag in physical_group_tags:
        print(f"Processing physical group with name '{gmsh.model.getPhysicalName(idim,pg_tag)}' | pg idimension = {idim}...")
        entity_tags = gmsh.model.getEntitiesForPhysicalGroup(idim, pg_tag)
        pg_name = gmsh.model.getPhysicalName(idim,pg_tag)                
        for tag in entity_tags:
          el_types, el_tags, el_node_tags = gmsh.model.mesh.getElements(idim,tag)
          for itype in range(len(el_tags)):
            elname = self._gmshElTypes[el_types[itype]] 
            el_nnodes = self._gmeshElTypeToNNodes[elname]
            el_node_tags[itype] = [int(nodtag-1) for nodtag in el_node_tags[itype]] # making it start from zero
            for iel in range(len(el_tags[itype])):
              el_node_tags_local = el_node_tags[itype][iel*el_nnodes:(iel+1)*el_nnodes]
              if idim == self.domainElDim:
                self.createEl(elname,pg_name,el_node_tags_local)
              else:
                self.createElBC(elname,pg_name,el_node_tags_local)

    return self.mesh

# ------------------------------------------------
# ------------------------------------------------

  def createEl(self,elname,pg_name,el_node_indices):
       
    if self.type == "TrussDSM":
      if elname != "line":
        DebugStop("TrussDSM should be a line")      
      E = self.physicalgroupToBC[pg_name]["E"]
      A = self.physicalgroupToBC[pg_name]["A"]
      tx = self.physicalgroupToBC[pg_name]["tx"]
      nodevec = [self.mesh.nodevec[nodind] for nodind in el_node_indices]
      el = TrussDSM(E=E,A=A,tx=tx,nodevec=nodevec)      

    elif self.type == "Bar2Node" or self.type == "Bar3Node":
      if elname != "line":
        DebugStop("Bar2Node or Bar3Node should be a line")      
      E = self.physicalgroupToBC[pg_name]["E"]
      A = self.physicalgroupToBC[pg_name]["A"]
      tx = self.physicalgroupToBC[pg_name]["tx"]
      nodevec = [self.mesh.nodevec[nodind] for nodind in el_node_indices]
      if self.type == "Bar2Node":
        el = Bar2Node(E=E,A=A,tx=tx,nodevec=nodevec)
      elif self.type == "Bar3Node":
        el = Bar3Node(E=E,A=A,tx=tx,nodevec=nodevec)
        DebugStop("Bar3Node was never tested. Please, comment this DebugStop and continue with caution")

    elif self.type == "Elas2D":
      if elname != "tria" and elname != "quad":
        DebugStop("Elas2D should be a tria or quad")
      E = self.physicalgroupToBC[pg_name]["E"]
      nu = self.physicalgroupToBC[pg_name]["nu"]
      b = self.physicalgroupToBC[pg_name]["b"]
      t = self.physicalgroupToBC[pg_name]["thickness"]
      isplanestress = self.physicalgroupToBC[pg_name]["isplanestress"]
      nodevec = [self.mesh.nodevec[nodind] for nodind in el_node_indices]
      if elname == "tria":
        el = ElasTria3(E=E,nu=nu,b=b,nodevec=nodevec,isplanestress=isplanestress,t=t)
      elif elname == "quad":
        el = ElasQuad4(E=E,nu=nu,b=b,nodevec=nodevec,isplanestress=isplanestress,t=t)
      
    elif self.type == "Elas3D":
      DebugStop("Reader for 3D elements not implemented yet.")

    self.mesh.addEl(el)      


# ------------------------------------------------
# ------------------------------------------------

  def createElBC(self,elname,pg_name,el_node_indices):
    if self.type == "TrussDSM":
      if elname != "node":
        DebugStop("TrussDSMBC should be a node")            
      type = self.physicalgroupToBC[pg_name]["type"]
      val = self.physicalgroupToBC[pg_name]["val"]      
      nodevec = [self.mesh.nodevec[nodind] for nodind in el_node_indices]
      el = TrussDSMBC(nodevec=nodevec,type=type,val=val)
      
    elif self.type == "Bar2Node" or self.type == "Bar3Node":
      if elname != "node":
        DebugStop("BarBC should be a node")            
      type = self.physicalgroupToBC[pg_name]["type"]
      val = self.physicalgroupToBC[pg_name]["val"]      
      nodevec = [self.mesh.nodevec[nodind] for nodind in el_node_indices]
      el = BarBC(nodevec=nodevec,type=type,val=val)      
    elif self.type == "Elas2D":
      if elname == "line":
        type = self.physicalgroupToBC[pg_name]["type"]
        val = self.physicalgroupToBC[pg_name]["val"]      
        nodevec = [self.mesh.nodevec[nodind] for nodind in el_node_indices]
        el = ElasBC(nodevec=nodevec,type=type,val=val)
      elif elname == "node":
        type = self.physicalgroupToBC[pg_name]["type"]
        val = self.physicalgroupToBC[pg_name]["val"]      
        nodevec = [self.mesh.nodevec[nodind] for nodind in el_node_indices]
        el = ElasPtBC(nodevec=nodevec,type=type,val=val)
        
    elif self.type == "Elas3D":
      DebugStop("Reader for 3D elements not implemented yet.")

    self.mesh.addEl(el)
  