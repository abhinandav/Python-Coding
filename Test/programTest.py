from program import reverse
import unittest

class TestReverse(unittest.TestCase):
    def test_reverse1(self):
        self.assertEqual(reverse([1, 2, 3, 4, 5, 6]), [6, 5, 4, 3, 2, 1])

    def test_reverse2(self):
        self.assertEqual(reverse([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])


    def test_reverse3(self):
        self.assertEqual(reverse([1, 2]), [2, 1])


if __name__ == '__main__':
    unittest.main()