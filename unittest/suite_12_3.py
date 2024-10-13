import tests_12_3
import unittest


suiteST = unittest.TestSuite()

suiteST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
suiteST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suiteST)
