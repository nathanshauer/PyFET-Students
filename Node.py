from .OOInterface import *
import numpy as np
import numpy.typing as npt

class Node(OOInterface):
  """ Node class, used to hold index and coordinates of a node in a mesh
  """
#   ****************** 
#      INITIALIZER
#   ******************    
  def __init__(self, coord: npt.NDArray = np.empty([0])):
    """Initializer for Node class

    Args:
        coord (npt.NDArray, optional): coordinates (x,y,z) of the node. Defaults to np.empty([0]).
    """
    super().__init__()
    self.index = -1 # index of the node in the mesh node vector
    self.coord = coord # coordinates of the node
    super().activateChecks()

#   ****************** 
#        METHODS
#   ******************     
  def __str__(self) -> str:
    return f"* Node index {self.index} \n coord = {self.coord}\n"
  
