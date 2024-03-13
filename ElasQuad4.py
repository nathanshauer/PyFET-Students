from .Elas import *
from .IntRuleQuad import *
import numpy as np
from numpy import linalg as LA

class ElasQuad4(Elas):
  """Class to manage shape functions of a 4-noded quadrilateral element
  """
#   ****************** 
#      INITIALIZER
#   ******************
  def __init__(self, E: float = -1., nu: float = -1., isplanestress: bool = True, b: list[float] = [0,0], nodevec: list[int] = []):
    """Initializer for ElasQuad4 class

    Args:
        E (float, optional): Young modulus. Defaults to -1..
        nu (float, optional): Poisson's ratio. Defaults to -1..
        isplanestress (bool, optional): plane stress of plane strain. Defaults to True.
        b (list[float], optional): body force. Defaults to [0,0].
        nodevec (list[int], optional): element node vector. Defaults to [].
    """
    if len(nodevec) != 4:
      DebugStop("Inconsistent nodevec vector")
        
    super().__init__(E=E,nu=nu,isplanestress=isplanestress,b=b,nodevec=nodevec)
    super().deactivateChecks()
    self.pord = 2 # minimum number of integration points in the case of linear element
    super().activateChecks()
     
#   ****************** 
#        METHODS
#   ******************   
  def __str__(self):    
    return f"Print => {self.__class__.__name__} (pord = {self.pord})\n" + super().__str__()
  
# ------------------------------------------------
# ------------------------------------------------

  def qsinod(self, nodind: int)->list[float]:
    if nodind < 0 or nodind > 3:
      DebugStop("Invalid node index")
    if nodind == 0:
      return [-1,-1.]
    elif nodind == 1:
      return [1.,-1.]
    elif nodind == 2:
      return [1.,1.]
    elif nodind == 3:
      return [-1.,1.]
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
    return [0,1,2,3]

# ------------------------------------------------
# ------------------------------------------------

  def vtktype(self) -> int:
    return 9

# ------------------------------------------------
# ------------------------------------------------
  
  def intrule(self):        
    return IntRuleQuad(self.pord)

# ------------------------------------------------
# ------------------------------------------------  