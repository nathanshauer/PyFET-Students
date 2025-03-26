from .Elas import *

class ElasPtBC(Elas):
  """0D point Boundary condition for Elas elements
  """
#   ****************** 
#      INITIALIZER
#   ******************
  def __init__(self, nodevec: list[Node] = [], type: str = "None", val: list[float] = [], E: float = 0., nu: float = 0.):    
    """Initializer for ElasPtBC

    Args:
        nodevec (list[Node], optional): node vector. Defaults to [].
        type (str, optional): Type of boundary condition (Displacement, Load, etc.). Defaults to "None".
        val (list[float], optional): Value to be applied at the boundary condition. Defaults to [].
        E (float, optional): Young modulus. Defaults to 0..
        nu (float, optional): Poisson's ratio. Defaults to 0..
    """    
    super().__init__(E=E,nu=nu,nodevec=nodevec)
    super().deactivateChecks()
    self.type = type
    if len(val) != 2:
      DebugStop("Val must have 2 position")
    self.val = val
    self.dim = 0
    super().activateChecks()  

#   ****************** 
#        METHODS
#   ******************   
  def calcstiff(self)->tuple[np.ndarray,np.ndarray]:

    # Create kel and fel with the right sizes and compute them. Then, return them both
    # Note that for elasticity, each node has two directions x and y    

    if self.type == "Displacement":
      DebugStop("YOUR CODE GOES HERE")
    elif self.type == "Load":
      DebugStop("YOUR CODE GOES HERE")
    elif self.type == "DisplacementX":
      DebugStop("YOUR CODE GOES HERE")
    elif self.type == "DisplacementY":
      DebugStop("YOUR CODE GOES HERE")
    else:
      DebugStop("Not defined or implemented boundary condition")

    # return kel, fel

# ------------------------------------------------
# ------------------------------------------------

  def vtktype(self) -> int:
    return 1 # 1 is the tag for points in vtk

# ------------------------------------------------
# ------------------------------------------------
# Methods that come from abstract class Element 
# and need to be implemented but are not used

  def jacobian(self, qsivec: list[float], dNdqsi: list[float])->tuple[float,list[float],list[float]]:
    DebugStop("Should not be called")

# ------------------------------------------------
# ------------------------------------------------
  
  def nodeorder(self)->list[int]:
    DebugStop("Should not be called")

# ------------------------------------------------
# ------------------------------------------------
    
  def qsinod(self, nodind: int)->list[float]:
    DebugStop("Should not be called")

# ------------------------------------------------
# ------------------------------------------------    

  def shape(self, qsivec: list[float])->tuple[list[float],list[float]]:
    DebugStop("Should not be called")

# ------------------------------------------------
# ------------------------------------------------
    
  def intrule(self):    
    DebugStop("Should not be called")

# ------------------------------------------------
# ------------------------------------------------        