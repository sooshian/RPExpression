import unittest
import RPN

class RPNtest(unittest.TestCase):
	def setUp(self,):
		self.tfunc = RPN.ToRPExp

	def tearDown(self,):
		pass

	def testfunc(self,):
		self.assertEqual(self.tfunc('9+(3-1)*3+10/2'),'9 3 1 - 3 * + 10 2 / +','fail')

if __name__ == '__main__':
	unittest.main()