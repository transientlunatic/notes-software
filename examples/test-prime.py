import unittest
from prime import is_prime

class PrimeTests(unittest.TestCase):
    """Test prime number checking."""

    def test_number_two(self):
        """Test that two is prime."""
        self.assertTrue(is_prime(2))

    def test_number_one(self):
        """Test that one is not prime."""
        self.assertFalse(is_prime(1))

    def test_number_zero(self):
        """Test that zero is not prime."""
        self.assertFalse(is_prime(0))

    def test_number_negative(self):
        """Test that negative numbers are not prime."""
        self.assertFalse(is_prime(-3))

    def test_actual_prime(self):
        """Test that a known prime is prime."""
        self.assertTrue(is_prime(13))
