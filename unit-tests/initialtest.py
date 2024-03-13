import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

# This code should run even in the raw student version of PyFET.
from PyFET.Node import *

def main():
  n1 = Node([1,0])
  print(f"node n1 = \n{n1}")
  print("PyFET is working properly.")

if __name__ == "__main__":
  main()