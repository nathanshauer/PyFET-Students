import numpy as np
import math
from .OOInterface import *

class IntRule1D(OOInterface):
  """Class used to generate integration rule for 1D elements
  """
#   ****************** 
#      INITIALIZER
#   ******************    
  def __init__(self, porder: int):
    """Initializer for IntRule1D class

    Args:
        porder (int): polynomial order to integrate
    """
    super().__init__()
    super().deactivateChecks()
    self.porder = porder

    DebugStop("YOUR CODE GOES HERE")   

    # Calculate the number of points and the Gauss-Legendre quadrature points and weights
    self.num_points = None  # Fill this attribute!

    # Generate integration rule with points organized as self.x = [[],[],[],...] and weights organizes as self.w = [,,,...]
    self.x = None # Fill this attribute!
    self.w = None # Fill this attribute!
    
    super().activateChecks()
    
#   ****************** 
#        METHODS
#   ******************      
  def rule(self):
    # Calculate the Gauss-Legendre quadrature points and weights
    return self.x, self.w

  def numPoints(self):
    return self.num_points