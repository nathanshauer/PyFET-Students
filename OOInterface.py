from dataclasses import dataclass

@dataclass
class OOInterface:
  """
  Class used to check if an attribute exists in class
  Used to avoid typos and accessing non existing attributes
  """
  check: bool = False

  def __setattr__(self, name, value):
    if self.check == True:
      if hasattr(self, name):
        super().__setattr__(name, value)
      else:            
        raise AttributeError(f"\n\n===> ERROR: Class {self.__class__.__name__} has no attribute {name}\n")
    else:
      super().__setattr__(name, value)
      
  
  def activateChecks(self): 
    self.check = True
  def deactivateChecks(self): 
    self.check = False
      
def DebugStop(message: str = ""):
  message = "\n\n==========> ERROR! " + message + "\n"
  raise ValueError(message)