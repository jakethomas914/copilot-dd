import unittest
from prime import is_prime

# FILE: test_prime.py


class TestIsPrime(unittest.TestCase):
    def test_zero(self):
        self.assertFalse(is_prime(0))

    def test_one(self):
        self.assertFalse(is_prime(1))

    def test_two(self):
        self.assertTrue(is_prime(2))

    def test_three(self):
        self.assertTrue(is_prime(3))

    def test_four(self):
        self.assertFalse(is_prime(4))

    def test_large_prime(self):
        self.assertTrue(is_prime(29))

    def test_large_non_prime(self):
        self.assertFalse(is_prime(30))

    def test_negative_number(self):
        self.assertFalse(is_prime(-5))

    def test_prime_square_root(self):
        self.assertFalse(is_prime(49))

    def test_prime_large(self):
        self.assertTrue(is_prime(101))

if __name__ == '__main__':
    unittest.main()import unittest
from prime import is_prime

# FILE: test_prime.py


class TestIsPrime(unittest.TestCase):
    def test_zero(self):
        self.assertFalse(is_prime(0))

    def test_one(self):
        self.assertFalse(is_prime(1))

    def test_two(self):
        self.assertTrue(is_prime(2))

    def test_three(self):
        self.assertTrue(is_prime(3))

    def test_four(self):
        self.assertFalse(is_prime(4))

    def test_large_prime(self):
        self.assertTrue(is_prime(29))

    def test_large_non_prime(self):
        self.assertFalse(is_prime(30))

if __name__ == '__main__':
    unittest.main()