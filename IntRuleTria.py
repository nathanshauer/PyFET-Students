from .OOInterface import *
import numpy as np

class IntRuleTria(OOInterface):
  """Class used to generate integration rule for triangle elements
  """  
#   ******************
#      INITIALIZER
#   ******************
  def __init__(self, porder: int):
    """Initializer for IntRuleQuad class

    Args:
        porder (int): polynomial order to integrate
    """    
    super().deactivateChecks()
    self.porder = porder
    if self.porder == 1:
      self.num_points = 1
    elif self.porder == 2:
      self.num_points = 3
    elif self.porder == 3:
      self.num_points = 4
    elif self.porder == 4:
      self.num_points = 7      

    self.createGaussPoints()
    
    super().activateChecks()

#   ******************
#        METHODS
#   ******************
  def rule(self):
    return self.x, self.w
  
  def numPoints(self):
    return self.num_points
  
  def createGaussPoints(self):
    if self.num_points == 1:
      self.x = np.array([[1/3, 1/3]])
      self.w = [1/2]
    elif self.num_points == 3:
      DebugStop("YOUR CODE GOES HERE")
    elif self.num_points == 4:
      DebugStop("YOUR CODE GOES HERE")
    elif self.num_points == 7:
      DebugStop("YOUR CODE GOES HERE")