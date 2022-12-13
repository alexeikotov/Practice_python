from calculator import Complex
import unittest

class TestComplex(unittest.TestCase):
    
    def test_equal(self):
        first = Complex(2, 5)
        second = Complex(2, 5)
        self.assertEqual(first, second)
        
    def test_equal_img(self):
        first = Complex(2, 6)
        second = Complex(2, 5)
        self.assertNotEqual(first, second)  

    def test_str(self):
        self.assertEqual(str(Complex(3,2)), '3 + 2*j')

    def test_add(self):
        expected = '4 + (-4)*j'
        self.assertEqual(str(Complex(1,2).add(Complex(3,-6))), expected)
    
    def test_sub(self):
        expected = '(-4) + (-4)*j'
        self.assertEqual(str(Complex(-2,-2).sub(Complex(2,2))), expected)

    def test_mul(self):
        expected = '(-18) + 40*j'
        self.assertEqual(str(Complex(12,-2).mul(Complex(-2,3))), expected)

    def test_dev(self):
        expected = '(-0.5) + (-1.5)*j'
        self.assertEqual(str(Complex(4,-2).dev(Complex(-2,2))), expected)

    def test_mod(self):
        self.assertEqual(Complex(4,3).mod(),5.0)

if __name__ == "__main__":
  unittest.main()
