import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

import unittest

from PyFET.TrussDSMBC import *
from PyFET.Analysis import *
from PyFET.GmshReader import *
import driverTrussDSM
import driverBar
import drivergmshBar
import driverBar3Node
import drivergmshTrussDSM
import driverTria3
import driverQuad4
import drivergmshDam
import testintrule1d
import testintrulequad
import testintruletria

class PatchTestsDSM(unittest.TestCase):
  def test_simpletruss(self):
    u = driverTrussDSM.main()                
    self.assertLess(abs(u[0]), 1.e-8)
    self.assertLess(abs(u[1]), 1.e-8)
    self.assertLess(abs(u[2]), 1.e-8)
    self.assertLess(abs(u[3]), 1.e-8)
    self.assertAlmostEqual(u[4], 5.32548347e-4,delta=1.e-8)
    self.assertAlmostEqual(u[5], -8.0e-5,delta=1.e-8)

  def test_simpletruss_gmsh(self):
    u = drivergmshTrussDSM.main()                
    self.assertLess(abs(u[0]), 1.e-8)
    self.assertLess(abs(u[1]), 1.e-8)
    self.assertLess(abs(u[2]), 1.e-8)
    self.assertLess(abs(u[3]), 1.e-8)
    self.assertAlmostEqual(u[4], 3.06274173e-4,delta=1.e-8)
    self.assertAlmostEqual(u[5], -8.0e-5,delta=1.e-8)

class PatchTestsBar(unittest.TestCase):
  def test_simplebar(self):      
    u = driverBar.main()
    self.assertLess(abs(u[0]), 1.e-8)      
    self.assertLess(abs(u[2]), 1.e-8)
    self.assertAlmostEqual(u[1], 9.0e-5,delta=1.e-8)

  def test_simplebar_gmsh(self):      
    u = drivergmshBar.main()
    self.assertLess(abs(u[0]), 1.e-8)      
    self.assertLess(abs(u[2]), 1.e-8)
    self.assertAlmostEqual(u[1], 3.0e-5,delta=1.e-8)      

  def test_simplebar_3node(self):      
    u = driverBar3Node.main()
    self.assertLess(abs(u[0]), 1.e-8)      
    self.assertLess(abs(u[2]), 1.e-8)
    self.assertAlmostEqual(u[1], 9.0e-5,delta=1.e-8)
    self.assertAlmostEqual(u[3], 9.0e-5,delta=1.e-8)
    self.assertAlmostEqual(u[4], 5.0e-5,delta=1.e-8)

class PatchTestsElas2D(unittest.TestCase):
  def test_simple_tria3(self):
    u = driverTria3.main()
    self.assertLess(abs(u[0]), 1.e-8)      
    self.assertLess(abs(u[1]), 1.e-8)      
    self.assertLess(abs(u[3]), 1.e-8)
    self.assertLess(abs(u[4]), 1.e-8)
    self.assertAlmostEqual(u[2], 1.2e-4,delta=1.e-8)
    self.assertAlmostEqual(u[5], -3.6e-5,delta=1.e-8)
    self.assertAlmostEqual(u[6], 1.2e-4,delta=1.e-8)
    self.assertAlmostEqual(u[7], -3.6e-5,delta=1.e-8)

  def test_dam_tria3_gmsh(self):
    u = drivergmshDam.main(simtype="Tria",isCoarse=True)
    self.assertLess(abs(u[0]), 1.e-8)      
    self.assertLess(abs(u[1]), 1.e-8)      
    self.assertLess(abs(u[2]), 1.e-8)
    self.assertLess(abs(u[3]), 1.e-8)
    self.assertAlmostEqual(u[4], 2.46090675e-04,delta=1.e-8)
    self.assertAlmostEqual(u[5], -4.51199216e-06,delta=1.e-8)
    self.assertAlmostEqual(u[6], 3.52032373e-04,delta=1.e-8)
    self.assertAlmostEqual(u[7], -3.80156038e-06,delta=1.e-8)
    self.assertAlmostEqual(u[8], 3.52023087e-04,delta=1.e-8)
    self.assertAlmostEqual(u[9], 6.79406411e-05,delta=1.e-8)

  def test_simple_quad4(self):
    u = driverQuad4.main()
    self.assertLess(abs(u[0]), 1.e-8)      
    self.assertLess(abs(u[1]), 1.e-8)      
    self.assertLess(abs(u[3]), 1.e-8)
    self.assertLess(abs(u[6]), 1.e-8)
    self.assertAlmostEqual(u[2], 1.2e-4,delta=1.e-8)
    self.assertAlmostEqual(u[5], -3.6e-5,delta=1.e-8)
    self.assertAlmostEqual(u[4], 1.2e-4,delta=1.e-8)
    self.assertAlmostEqual(u[7], -3.6e-5,delta=1.e-8)

  def test_dam_quad4_gmsh(self):
    u = drivergmshDam.main(simtype="Quad",isCoarse=True)
    sumofu = np.sum(u)    
    self.assertAlmostEqual(sumofu, 0.007811570123819315,delta=1.e-8)

class IntRules(unittest.TestCase):
  def test_intrule1d(self):
    integral = testintrule1d.main()
    self.assertAlmostEqual(integral, 3.0666666666666673,delta=1.e-8)

  def test_intrulequad(self):
    integral = testintrulequad.main()
    self.assertAlmostEqual(integral, 0.6044444444444448,delta=1.e-8)

  def test_intruletria(self):
    integral = testintruletria.main()
    self.assertAlmostEqual(integral, 0.541666666666667,delta=1.e-8)

if __name__ == "__main__":
  unittest.main()