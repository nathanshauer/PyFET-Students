from .Elas import *
from .IntRuleTria import *
import numpy as np
from numpy import linalg as LA

class ElasTria3(Elas):
  """Class to manage shape functions of a 3-noded triangular element
  """
#   ****************** 
#      INITIALIZER
#   ******************
  def __init__(self, E: float = -1., nu: float = -1., isplanestress: bool = True, b: list[float] = [0,0], nodevec: list[int] = [], t = 1.0):
    """Initializer for ElasTria3 class
    
    Args:
        E (float, optional): Young modulus. Defaults to -1..
        nu (float, optional): Poisson's ratio. Defaults to -1..
        isplanestress (bool, optional): plane stress of plane strain. Defaults to True.
        b (list[float], optional): body force. Defaults to [0,0].
        nodevec (list[int], optional): element node vector. Defaults to [].
    """
    if len(nodevec) != 3: # bc points, bc line, and element with 3 nodes
      DebugStop("Inconsistent nodevec vector")
        
    super().__init__(E=E,nu=nu,isplanestress=isplanestress,b=b,nodevec=nodevec,t=t)
    super().deactivateChecks()
    self.pord = 1 # minimum number of integration points in the case of linear element
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
    if nodind == 0:
      return [1.,0.]
    elif nodind == 1:
      return [0.,1.]  
    elif nodind == 2:
      return [0.,0.]
    else:
      DebugStop("Invalid node index")

# ------------------------------------------------
# ------------------------------------------------
  
  def shape(self, qsivec: list[float])->tuple[list[float],list[float]]:
    DebugStop("YOUR CODE GOES HERE")
    # Compute shape functions, N and derivatives dNdqsi
    
    # return N, dNdqsi

# ------------------------------------------------
# ------------------------------------------------

  def nodeorder(self) -> list[int]:
    return [0,1,2]

# ------------------------------------------------
# ------------------------------------------------

  def vtktype(self) -> int:
    return 5

# ------------------------------------------------
# ------------------------------------------------
  
  def intrule(self):        
    return IntRuleTria(self.pord)

# ------------------------------------------------
# ------------------------------------------------  
