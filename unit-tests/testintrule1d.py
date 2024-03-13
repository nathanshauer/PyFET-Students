import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from PyFET.IntRule1D import *

def f(x):
  return 1 + x + x**2 + x**3 + x**4

def main():
  intrule = IntRule1D(porder=4)
  x,w = intrule.rule()
  print(x,w)
  integral = 0
  for i in range(intrule.numPoints()):
    integral += f(x[i])*w[i]
  
  print(f"integral = {integral}")
  
  return integral

if __name__ == "__main__":
  main()