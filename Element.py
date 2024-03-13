from .OOInterface import *
from .Node import *
from abc import ABC, abstractmethod


class Element(ABC,OOInterface):
  """
  Abstract element class
  Used to set necessary methods for an element
  """
#   ****************** 
#      INITIALIZER
#   ******************
  def __init__(self, nodevec: list[Node] = [], dim: int = -1):
    """Initializer for Element

    Args:
        nodevec (list[Node], optional): Vector with nodes. Defaults to [].
        dim (int, optional): Element dimension. Defaults to -1.
    """
    super().__init__()
    self.index = -1 # element index
    self.dim = dim # element dimension
    self.nodevec = nodevec # element nodes
    self.eft = None # element freedom table
    self._bignumber = 1.e12 # big number for boundary condition imposition
    self.pord = -1 # order of the element
    super().activateChecks()
  
#   ****************** 
#        METHODS
#   ******************      
  def __str__(self):
    mystr = f"\n--------> Element index {self.index}\ndim = {self.dim}\nNodes: {self.nnodes()}\n"
    nodes = "".join([node.__str__() for node in self.nodevec])  
    mystr += nodes
    return mystr

# ------------------------------------------------
# ------------------------------------------------

  def nnodes(self)->int:
    """Returns number of nodes in the element

    Returns:
        int: number of nodes
    """
    return len(self.nodevec)

# ------------------------------------------------
# ------------------------------------------------

  def ndofs(self)->int:
    """Returns number of degrees of freedom of the element

    Returns:
        int: number of degrees of freedom
    """
    
    sum = 0
    DebugStop("YOUR CODE GOES HERE")
    # For each node, sum the number of state variables
    return sum

# ------------------------------------------------
# ------------------------------------------------

  def buildEFT(self):
    """Builds the element freedom table
    """

    DebugStop("YOUR CODE GOES HERE")
    # Initialize the eft size with the number of dofs
    # Note you will need to fill the attribute self.eft
      
    # Compute the eft based on the node.index and the number of state variables
    # position the eft is compute as node.index*self.nstatevar() + state_variable_index

# ------------------------------------------------
# ------------------------------------------------
  
  def xmap(self, qsivec: list[float]) -> list[float]:
    """Computes X mapping at a point qsivec

    Args:
        qsivec (list[float]): points in master element coordinates

    Returns:
        list[float]: point in physical coordinates
    """
    N, dNdqsi = self.shape(qsivec)
    # build element coordinate vector
    if self.dim == 1:
      elnodevec = np.array([self.nodevec[i].coord for i in range(self.nnodes())])
    elif self.dim == 2:
      elnodevec = np.zeros(self.ndofs())
      for i in range(self.nnodes()):
        elnodevec[2*i] = self.nodevec[i].coord[0]
        elnodevec[2*i+1] = self.nodevec[i].coord[1]
    elif self.dim == 3:
      elnodevec = np.zeros(self.ndofs())
      for i in range(self.nnodes()):
        elnodevec[2*i] = self.nodevec[i].coord[0]
        elnodevec[2*i+1] = self.nodevec[i].coord[1]
        elnodevec[2*i+2] = self.nodevec[i].coord[2]
    x = N @ elnodevec
    return x
  
  def calcstiff(self):
    """Computes the element stiffness matrix
    """
    DebugStop("YOUR CODE GOES HERE")

    # Get the integration rule
    # Initialize kel and fel with zeros and the correct dimensions
    # Loop over all integration points
    # Compute the shape functions and their derivatives
    # Compute the jacobian matrix
    # Compute the physical derivatives  
    # Compute the B matrix
    # Add contribution of the integration point to the element 
    # stiffness matrix and load vector
    # return kel, fel       

# ------------------------------------------------
# ------------------------------------------------  

#   ****************** 
#    ABSTRACT METHODS
#   ******************   

  @abstractmethod
  def nstatevar(self)->int:
    """Element number of state variables at each node.
    """
    pass

# ------------------------------------------------
# ------------------------------------------------

  @abstractmethod
  def shape(self, qsivec: list[float])->tuple[list[float],list[float]]:
    """Computes the value of the shape functions and their derivatives at a point qsivec

    Args:
        qsivec (list[float]): point in master element coordinates

    Returns:
        list[float]: shape functions and their derivatives
    """
    pass      

# ------------------------------------------------
# ------------------------------------------------
  
  @abstractmethod
  def jacobian(self, qsivec: list[float], dNdqsi: list[float])->tuple[float,list[float],list[float]]:
    """Computes the jacobian matrix at a point qsivec

    Args:
        qsivec (list[float]): point in master element coordinates
        dNdqsi (list[float]): shape functions derivatives in element coordinates

    Returns:
        tuple[float,list[float],list[float]]: jac, invjac, detjac (jacobian matrix, inverse jacobian matrix, and jacobian determinant)
    """
    pass      

# ------------------------------------------------
# ------------------------------------------------  

  @abstractmethod
  def vtktype(self)->int:
    """Int that defines the VTK type of the element

    Returns:
        int: VTK type
    """
    pass

# ------------------------------------------------
# ------------------------------------------------

  @abstractmethod
  def postprocvar(self, var, qsivec: list[float], ue: list[float])->list[float]:
    """Computes a post processing variable with name var at a point qsivec

    Args:
        var (_type_): name of the post processing variable
        qsivec (list[float]): point in master element coordinates
        ue (list[float]): element solution vector

    Returns:
        list[float]: post processed variable
    """
    pass

# ------------------------------------------------
# ------------------------------------------------

  @abstractmethod
  def qsinod(self, nodind: int)->list[float]:
    """Returns the master element coordinate of a node

    Args:
        nodind (int): node index

    Returns:
        list[float]: master element coordinate
    """
    pass

# ------------------------------------------------
# ------------------------------------------------

  @abstractmethod
  def nodeorder(self)->list[int]:
    """Returns the node order for the element used in VTK (used for postprocessing mostly)

    Returns:
        list[int]: node order
    """
    pass

# ------------------------------------------------
# ------------------------------------------------
  
  @abstractmethod
  def intrule(self):
    """Returns the integration rule for the element

    Returns:
        IntRule object with qsi points and weights
    """
    pass

# ------------------------------------------------
# ------------------------------------------------  