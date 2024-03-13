import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from PyFET.IntRuleQuad import *

def f(x,y):
  return x+y + x**2 * y**2 + x**3 * y**3 + x**4 * y**4

def main():
  intrule = IntRuleQuad(porder=4)
  xvec,wvec = intrule.rule()
  print(xvec,wvec)
  integral = 0
  for i in range(intrule.numPoints()):
    x = xvec[i,0]
    y = xvec[i,1]
    w = wvec[i]
    integral += f(x,y)*w

  print(f"integral = {integral}")  

  return integral

if __name__ == "__main__":
  main()