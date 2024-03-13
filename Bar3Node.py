from .Bar import *
from .IntRule1D import *
import numpy as np
from numpy import linalg as LA

# CHALLENGE: Implement qudratic bar element
class Bar3Node(Bar):
  """Implements necessary methods for a 3-node bar element.
  """  
#   ****************** 
#      INITIALIZER
#   ******************
  def __init__(self, E: float = -1., A: float = -1., tx: float = 0., nodevec: list[int] = []):
    """Initializer for Bar2Node element.

    Args:
        E (float, optional): Young modulus. Defaults to -1..
        A (float, optional): Section area. Defaults to -1..
        tx (float, optional): Distribute load. Defaults to 0..
        nodevec (list[int], optional): node vector. Defaults to [].
    """
    if len(nodevec) > 3 or len(nodevec) < 1:
      DebugStop("Inconsistent nodevec vector")
        
    super().__init__(nodevec=nodevec,E=E,A=A,tx=tx)
    super().deactivateChecks()
    self.pord = 2 # order of the element
    super().activateChecks()
 
#   ****************** 
#        METHODS
#   ******************   
  def __str__(self):    
    return f"Print => {self.__class__.__name__} (pord = {self.pord})\n" + super().__str__()
  
# ------------------------------------------------
# ------------------------------------------------

  def qsinod(self, nodind: int)->list[float]:
    if nodind < 0 or nodind > 2:
      DebugStop("Invalid node index")
 
    DebugStop("YOUR CODE GOES HERE")   
    # nodind 0 should return [-1,0], nodind 1 should return [0,0] and nodind 2 should return [1,0]
    
# ------------------------------------------------
# ------------------------------------------------
  
  def shape(self, qsivec: list[float])->tuple[list[float],list[float]]:
    DebugStop("YOUR CODE GOES HERE")   

# ------------------------------------------------
# ------------------------------------------------
  
  def nodeorder(self) -> list[int]:
    return [0,2,1] # vtk expects nodes in this order

# ------------------------------------------------
# ------------------------------------------------  
  
  def vtktype(self) -> int:
    return 21

# ------------------------------------------------
# ------------------------------------------------