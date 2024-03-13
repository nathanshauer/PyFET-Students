import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from PyFET.IntRuleTria import *

def f(x,y):
  return x+y + x**2 + y**2 + x*y

def main():
  intrule = IntRuleTria(porder=3)
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