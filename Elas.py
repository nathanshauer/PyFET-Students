from .Element import *
from .IntRuleTria import *
from .IntRuleQuad import *
import numpy as np
from numpy import linalg as LA

class Elas(Element):
  """Elasticity element class for 2D simulations.
  """
#   ****************** 
#      INITIALIZER
#   ******************
  def __init__(self, E: float = -1., nu: float = -1., isplanestress: bool = True, b: list[float] = [0,0], nodevec: list[int] = [], t: float = 1.0):
    """Initializer for Elasticity element.

    Args:
        E (float, optional): Young modulus. Defaults to -1..
        nu (float, optional): Poisson's ratio. Defaults to -1..
        isplanestress (bool, optional): boolean stating if it is plane stress. Defaults to True.
        b (list[float], optional): body force. Defaults to [0,0].
        nodevec (list[int], optional): element node vector. Defaults to [].
    """
    if E < 0 or nu < 0 or nu > 0.5:
      DebugStop("Inconsistent material properties")
    if len(nodevec) > 0:
      if (False in [len(nod.coord) == 2 or len(nod.coord) == 3 for nod in nodevec]):
        DebugStop("Nodes should always have two coordinates (x,y) for Bar simulations")
        
    super().__init__(nodevec=nodevec,dim=2)
    super().deactivateChecks()
    self.E = E # Young modulus
    self.nu = nu # Poisson's ratio
    self.b = b # body force
    self.isplanestress = isplanestress # plane stress or plane strain
    self.t = t # thickness
    self.Dmat = self.createDmat(E,nu,isplanestress) # constitutive matrix
    super().activateChecks()
 
  def createDmat(self, E: float, nu: float, isplanestress: bool)->np.array:
    DebugStop("YOUR CODE GOES HERE")
    # return Dmat
    
#   ****************** 
#        METHODS
#   ******************   
  def __str__(self):    
    return f"Material Properties:\n E = {self.E}, nu = {self.nu}, t = {self.t}, isplanestress = {self.isplanestress}, Dmat = {self.Dmat}" + super().__str__()
  
# ------------------------------------------------
# ------------------------------------------------

  def physicalDerivatives(self, dNdqsi: list[float], invjac: float)->np.array:    
    DebugStop("YOUR CODE GOES HERE")
    # return dNdx

# ------------------------------------------------
# ------------------------------------------------

  def createB(self, dNdx: list[float])->np.array:
    DebugStop("YOUR CODE GOES HERE")
    # return B
  
# ------------------------------------------------
# ------------------------------------------------

  def jacobian(self, qsivec: list[float], dNdqsi: list[float])->tuple[float,list[float],list[float]]:
        
    DebugStop("YOUR CODE GOES HERE")    
    # return jac, invjac, detjac
  
# ------------------------------------------------
# ------------------------------------------------

  def postprocvar(self, var, qsivec: list[float], ue: list[float])->list[float]:
    N, dNdqsi = self.shape(qsivec)
    if var == "displacement" or var == "solution":
      DebugStop("YOUR CODE GOES HERE")
      # return upt
    elif var == "strainxx" or var == "strainyy" or var == "strainxy" or var == "stressxx" or var == "stressyy" or var == "stressxy":
      DebugStop("YOUR CODE GOES HERE")
      if var == "strainxx":
        DebugStop("YOUR CODE GOES HERE")        
      elif var == "strainyy":
        DebugStop("YOUR CODE GOES HERE")
      elif var == "strainxy":
        DebugStop("YOUR CODE GOES HERE")
      if var == "stressxx" or "stressyy" or "stressxy":
        DebugStop("YOUR CODE GOES HERE")
        if var == "stressxx":
          DebugStop("YOUR CODE GOES HERE")
        elif var == "stressyy":
          DebugStop("YOUR CODE GOES HERE")
        elif var == "stressxy":
          DebugStop("YOUR CODE GOES HERE")
    else:
      DebugStop("Variable not implemented")

# ------------------------------------------------
# ------------------------------------------------
      
  def nstatevar(self):
    return 2 # u and v at each node

# ------------------------------------------------
# ------------------------------------------------
  
  
