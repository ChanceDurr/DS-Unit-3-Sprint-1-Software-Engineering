import unittest
from mod import *

class TestShirtTypes(unittest.TestCase):
    
    def test_shirt(self):
        self.assertEqual(type(Shirt('t-shirt').material), str)
        self.assertEqual(type(Shirt('t-shirt').size), str)
        self.assertEqual(type(Shirt('t-shirt').sleeve), str)
        self.assertEqual(type(Shirt('t-shirt').style), str)

    def test_Complex(self):
        self.assertEqual(Complex(1, 2).add(), 3)
        self.assertEqual(Complex(1, 2).subtract(), 1)
        self.assertEqual(Complex(2, 4).divide(), 2)

if __name__ == '__main__':
    unittest.main()