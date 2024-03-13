import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from PyFET.TrussDSMBC import *
from PyFET.Analysis import *
from PyFET.GmshReader import *

def main():
  # Creating nodes
  n0 = Node(coord=np.array([0.,0.]))
  n1 = Node(coord=np.array([2.,0.]))
  n2 = Node(coord=np.array([2.,2.]))

  # Creating elements
  el0 = TrussDSM(E=25000.,A=1.,nodevec=[n0,n1],tx=0)
  el1 = TrussDSM(E=25000.,A=1.,nodevec=[n1,n2],tx=0)
  el2 = TrussDSM(E=25000.,A=1.,nodevec=[n2,n0],tx=-1)
  
  # Creating BCs
  bc0 = TrussDSMBC(E=25000,A=1,nodevec=[n0],type="Displacement",val=[0.,0.])
  # bc1 = TrussDSMBC(E=25000,A=1,nodevec=[n2],type="Displacement",val=[0.,0.])
  bc2 = TrussDSMBC(E=25000,A=1,nodevec=[n1],type="DisplacementY",val=[0.,0.])
  bcForce = TrussDSMBC(E=25000,A=1,nodevec=[n2],type="Load",val=[1.,0.])

  # Creating mesh
  mesh = Mesh(dim=2)
  mesh.addNode(n0)
  mesh.addNode(n1)
  mesh.addNode(n2)
  mesh.addEl(el0)
  mesh.addEl(el1)
  mesh.addEl(el2)
  
  mesh.addEl(bc0)
  # mesh.addEl(bc1)
  mesh.addEl(bc2)
  mesh.addEl(bcForce)

  # Printing mesh in vtk format
  mesh.generateGeometryVTK("mesh.vtk")
  # print(mesh)

  # Solve problem
  analysis = Analysis(mesh=mesh)
  analysis.run()

  # Post process
  vecnames = ["displacement"]
  scalnames = ["normal", "strain"]
  analysis.generateSolutionVTK(filename="postproc.vtk",vecnames=vecnames,scalnames=scalnames)

  return analysis.u

if __name__ == "__main__":       
  main()