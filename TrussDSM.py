from .Element import *
import numpy as np
from numpy import linalg as LA

class TrussDSM(Element):
  """
  TrussDSM element class
  Implements the truss element through a structural analysis perspective
  """
#   ****************** 
#      INITIALIZER
#   ******************
  def __init__(self, E: float = -1., A: float = -1., tx: float = 0., nodevec: list[Node] = []):
    """Initializer for TrussDSM class

    Args:
        E (float, optional): Young modulus. Defaults to -1..
        A (float, optional): Section area. Defaults to -1..
        tx (float, optional): Distributed load. Defaults to 0..
        nodevec (list[int], optional): Vector with node objects. Defaults to [].  
    """
    if E < 0 or A < 0:
      DebugStop("Inconsistent material properties")
    if len(nodevec) > 2 and len(nodevec) < 1:
      DebugStop("Inconsistent nodevec vector")
    if len(nodevec) > 0:
      if (False in [len(nod.coord) == 2 or len(nod.coord) == 3 for nod in nodevec]):
        DebugStop("Nodes should always have two coordinates (x,y) for TrussDSM simulations")
        
    super().__init__(nodevec=nodevec,dim=2)
    super().deactivateChecks()
    self.E = E
    self.A = A
    self.tx = tx
    super().activateChecks()
 
#   ****************** 
#        METHODS
#   ******************   
  def __str__(self):    
    return super().__str__() + f"Material Properties:\n E = {self.E}, A = {self.A}, tx = {self.tx}"

# ------------------------------------------------
# ------------------------------------------------

  def qsinod(self, nodind: int)->list[float]:
    if nodind < 0 or nodind > 1:
      DebugStop("Invalid node index")
    return [nodind]

# ------------------------------------------------
# ------------------------------------------------

  def calcstiff(self):

    DebugStop("YOUR CODE GOES HERE")

    # Compute element length l
    # Compute direction cosines c and s
    # Compute element stiffness matrix kel
    # Compute element load vector fel
    # return kel, fel

# ------------------------------------------------
# ------------------------------------------------

  def nstatevar(self):
    return 2 # ux and uy (2d truss)

# ------------------------------------------------
# ------------------------------------------------

  def postprocvar(self, var, qsivec: list[float], ue: list[float])->list[float]:
    # Compute element lenght l
    # Compute direction cosines c and s
    # Compute Displacement Transformation Matrix
    
    if var == "displacement" or var == "solution":
      if qsivec[0] == 0:
        return ue[0:2]
      elif qsivec[0] == 1:
        return ue[2:4]
      else:
        DebugStop("Invalid qsivec")
    if var == "axialdisplacement":
      DebugStop("YOUR CODE GOES HERE")
    if var == "strain":
      DebugStop("YOUR CODE GOES HERE")            
      # return eps
    if var == "axialforce" or "normal":
      DebugStop("YOUR CODE GOES HERE")
      if qsivec[0] == 0:
        DebugStop("YOUR CODE GOES HERE")
        # Return the axial force in the node 0
      elif qsivec[0] == 1:
        DebugStop("YOUR CODE GOES HERE")
        # Return the axial force in the node 1
      else:
        DebugStop("Invalid qsivec") 

# ------------------------------------------------
# ------------------------------------------------

  def shape(self, qsivec: list[float])->tuple[list[float],list[float]]:
    DebugStop("TrussDSM element does not have shape functions")
    return [None]

# ------------------------------------------------
# ------------------------------------------------

  def nodeorder(self) -> list[int]:
    return [0,1]
  
# ------------------------------------------------
# ------------------------------------------------

  def vtktype(self) -> int:
    return 3

# ------------------------------------------------
# ------------------------------------------------

  def jacobian(self, qsivec: list[float], dNdqsi: list[float])->tuple[float,list[float],list[float]]:
    DebugStop("Should never be called in TrussDSM")
  
# ------------------------------------------------
# ------------------------------------------------
    
  def intrule(self):    
    DebugStop("Should never be called in TrussDSM")

# ------------------------------------------------
# ------------------------------------------------        