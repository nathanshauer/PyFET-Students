import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from PyFET.Bar3Node import *
from PyFET.Analysis import *
from PyFET.GmshReader import *

def main():
  # Creating nodes
  n0 = Node(coord=np.array([0.,0.]))
  n1 = Node(coord=np.array([3.,0.]))
  n2 = Node(coord=np.array([4.,0.]))
  
  n01 = Node(coord=np.array([1.5,0.]))
  n12 = Node(coord=np.array([3.5,0.]))

  # Creating elements
  el0 = Bar3Node(E=25000.,A=1.,nodevec=[n0,n01,n1],tx=1)
  el1 = Bar3Node(E=25000.,A=1.,nodevec=[n1,n12,n2],tx=1)
  # el2 = Bar(E=25000.,A=1.,nodevec=[n2,n0],tx=-1)
  
  # Creating BCs
  bc0 = BarBC(E=25000,A=1,nodevec=[n0],type="Displacement",val=[0.])
  bc1 = BarBC(E=25000,A=1,nodevec=[n2],type="Displacement",val=[0.])
  bcForce = BarBC(E=25000,A=1,nodevec=[n1],type="Load",val=[1.])

  # Creating mesh
  mesh = Mesh(dim=1)
  mesh.addNode(n0)
  mesh.addNode(n1)
  mesh.addNode(n2)
  mesh.addNode(n01)
  mesh.addNode(n12)
  
  mesh.addEl(el0)
  mesh.addEl(el1)
  
  mesh.addEl(bc0)
  mesh.addEl(bc1)
  mesh.addEl(bcForce)

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