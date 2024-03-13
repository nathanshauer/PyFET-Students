import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from PyFET.ElasPtBC import *
from PyFET.ElasBC import *
from PyFET.ElasQuad4 import *
from PyFET.Analysis import *
from PyFET.GmshReader import *

def main():
  # Creating nodes
  n0 = Node(coord=np.array([0.,0.]))
  n1 = Node(coord=np.array([3.,0.]))
  n2 = Node(coord=np.array([3.,3.]))
  n3 = Node(coord=np.array([0.,3.]))

  # Creating elements
  el0 = ElasQuad4(E=25000.,nu=0.3,nodevec=[n0,n1,n2,n3])
  
  # Creating BCs
  bc0 = ElasPtBC(E=25000,nu=0.3,nodevec=[n0],type="Displacement",val=[0.,0.])
  bc1 = ElasPtBC(E=25000,nu=0.3,nodevec=[n3],type="DisplacementX",val=[0.,0.])
  # bc0 = ElasBC(E=25000,nu=0.3,nodevec=[n0,n2],type="Displacement",val=[0.,0.])
  bcForce = ElasPtBC(E=25000,nu=0.3,nodevec=[n1],type="Load",val=[1.5,0.])
  bcForce2 = ElasPtBC(E=25000,nu=0.3,nodevec=[n2],type="Load",val=[1.5,0.])

  # Creating mesh
  mesh = Mesh(dim=2)
  mesh.addNode(n0)
  mesh.addNode(n1)
  mesh.addNode(n2)
  mesh.addNode(n3)
  mesh.addEl(el0)
  
  mesh.addEl(bc0)
  mesh.addEl(bc1)
  mesh.addEl(bcForce)
  mesh.addEl(bcForce2)

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
  main()