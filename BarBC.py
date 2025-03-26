from .Bar import *

class BarBC(Bar):
  """Boundary condition class for Bar elements
  """
#   ****************** 
#      INITIALIZER
#   ******************
  def __init__(self, nodevec: list[Node] = [], type: str = "None", val: list[float] = [], E: float = 0., A: float = 0.):    
    """Initializer for BarBC

    Args:
        nodevec (list[Node], optional): node vector. Defaults to [].
        type (str, optional): Type of boundary condition (Displacement, Load, etc.). Defaults to "None".
        val (list[float], optional): Value to be applied at the boundary condition. Defaults to [].
        E (float, optional): Young modulus. Defaults to 0..
        A (float, optional): Section area. Defaults to 0..
    """
    super().__init__(E=E,A=A,nodevec=nodevec)
    super().deactivateChecks()
    self.type = type
    if len(val) != 1:
      DebugStop("Val must have 1 position")
    self.val = val
    self.dim = 0
    super().activateChecks()  

#   ****************** 
#        METHODS
#   ******************   
  def calcstiff(self)->tuple[np.ndarray,np.ndarray]:
    DebugStop("YOUR CODE GOES HERE")   

    # Create kel and fel with the right sizes and compute them. Then, return them both
    
    if self.type == "Displacement":
      DebugStop("YOUR CODE GOES HERE")      
    elif self.type == "Load":
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