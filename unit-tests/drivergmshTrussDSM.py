import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from PyFET.TrussDSMBC import *
from PyFET.Analysis import *
from PyFET.GmshReader import *

def main():
  physicalgroupToBC = {
    "truss": {
      "E": 25000., "A": 1., "tx": 0.
    },
    "fixed": {
      "type": "Displacement",
      "val": [0.,0.]
    },
    "fixedy": {
      "type": "DisplacementY",
      "val": [0.,0.]
    },
    "force1": {
      "type": "Load",
      "val": [1.,0.]
    }
  }
  reader = GmshReader(physicalgroupToBC=physicalgroupToBC,type="TrussDSM")
  mesh = reader.readMesh(filename="simpletruss.msh")

  # Printing mesh in vtk format
  mesh.generateGeometryVTK("mesh.vtk")
  # print(mesh)

  # Solve problem
  analysis = Analysis(mesh=mesh)
  analysis.run()

  # Post process
  vecnames = ["displacement"]
  scalnames = ["normal", "strain", "stress"]
  analysis.generateSolutionVTK(filename="postproc.vtk",vecnames=vecnames,scalnames=scalnames)

  return analysis.u

if __name__ == "__main__":       
  main()