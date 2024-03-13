from .IntRule1D import *

class IntRuleQuad(IntRule1D):
  """Class used to generate integration rule for quadrilateral elements
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
    self.createQuadRuleFrom1DRule() # simply a helper function to not crowd the __init__ method
    self.num_points = len(self.w)
    super().activateChecks()

#   ******************
#        METHODS
#   ******************
  def rule(self):
    return self.x, self.w
  
  def createQuadRuleFrom1DRule(self):
    DebugStop("YOUR CODE GOES HERE")   
    
    # Calculate the number of points and the Gauss-Legendre quadrature points and weights for a 1D rule
    # The square integration rule is the tensor product of two 1D rules

    self.x = None # Fill this attribute at the end of this function!
    self.w = None # Fill this attribute at the end of this function!

  def numPoints(self):
    return self.num_points