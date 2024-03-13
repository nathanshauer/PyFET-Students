from .Element import *
from .IntRule1D import *
import numpy as np
from numpy import linalg as LA

class Bar(Element):
  """Bar element class for 1D simulations.
  """
#   ****************** 
#      INITIALIZER
#   ******************
  def __init__(self, E: float = -1., A: float = -1., tx: float = 0., nodevec: list[int] = []):
    """Initializer for Bar element.

    Args:
        E (float, optional): Young modulus. Defaults to -1..
        A (float, optional): Section area. Defaults to -1..
        tx (float, optional): Distribute load. Defaults to 0..
        nodevec (list[int], optional): Element nodes. Defaults to [].
    """
    if E < 0 or A < 0:
      DebugStop("Inconsistent material properties")
    if len(nodevec) > 0:
      if (False in [len(nod.coord) == 2 or len(nod.coord) == 3 for nod in nodevec]):
        DebugStop("Nodes should always have two coordinates (x,y) for Bar simulations")
        
    super().__init__(nodevec=nodevec,dim=1)
    super().deactivateChecks()
    self.E = E
    self.A = A
    self.Dmat = E * A
    self.tx = tx
    super().activateChecks()
 
#   ****************** 
#        METHODS
#   ******************   
  def __str__(self):    
    return f"Material Properties:\n E = {self.E}, A = {self.A}, tx = {self.tx}" + super().__str__()
    
# ------------------------------------------------
# ------------------------------------------------

  def physicalDerivatives(self, dNdqsi: list[float], invjac: float)->np.array:
    DebugStop("YOUR CODE GOES HERE")   

# ------------------------------------------------
# ------------------------------------------------

  def createB(self, dNdx: list[float])->np.array:
    DebugStop("YOUR CODE GOES HERE")   
  
# ------------------------------------------------
# ------------------------------------------------

  def jacobian(self, qsivec: list[float], dNdqsi: list[float])->tuple[float,list[float],list[float]]:
    # Assume equally spaced nodes for both Bar2Node and Bar3Node
    DebugStop("YOUR CODE GOES HERE")   
  
# ------------------------------------------------
# ------------------------------------------------

  def postprocvar(self, var, qsivec: list[float], ue: list[float])->list[float]:
    DebugStop("YOUR CODE GOES HERE")   

# ------------------------------------------------
# ------------------------------------------------
  
  def nstatevar(self):
    return 1 # only ux

# ------------------------------------------------
# ------------------------------------------------

  def intrule(self):    
    return IntRule1D(self.pord)

# ------------------------------------------------
# ------------------------------------------------
