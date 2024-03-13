import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from PyFET.ElasBC import *
from PyFET.Analysis import *
from PyFET.GmshReader import *

def main(simtype: str = "Tria", isCoarse: bool = False):
  
  physicalgroupToBC = {
    "dom": {
      "E": 25000., "nu": 0.3, "b": [0.,0.], "isplanestress": False
    },
    "fixed": {
      "type": "Displacement",
      "val": [0.,0.]
    },
    "load": {
      "type": "Load",
      "val": [1.,0.]
    }
  }
  reader = GmshReader(physicalgroupToBC=physicalgroupToBC,type="Elas2D")

  if isCoarse:
    if simtype == "Quad":
      mesh = reader.readMesh(filename="dam_quad_coarse.msh")
    elif simtype == "Tria":
      mesh = reader.readMesh(filename="dam_tria_coarse.msh")
    else:
      DebugStop("Not implemented")
  else:
    if simtype == "Quad":
      mesh = reader.readMesh(filename="dam_quad.msh")
    elif simtype == "Tria":
      mesh = reader.readMesh(filename="dam_tria.msh")
    else:
      DebugStop("Not implemented")

  # Printing mesh in vtk format
  mesh.generateGeometryVTK("mesh.vtk")
  # print(mesh)

  # Solve problem
  analysis = Analysis(mesh=mesh)
  analysis.run()

  # Post process
  vecnames = ["displacement"]
  scalnames = ["stressxx", "stressyy", "stressxy", "strainxx", "strainyy", "strainxy"]
  analysis.generateSolutionVTK(filename="postproc.vtk",vecnames=vecnames,scalnames=scalnames)

  return analysis.u

if __name__ == "__main__":       
  main(simtype="Quad", isCoarse=False)