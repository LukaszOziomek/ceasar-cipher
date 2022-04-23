import unittest
from cesar import encrypt


class TestEncrypt(unittest.TestCase):
    def test_simple_encrypt(self):
        self.assertEqual(encrypt("A", 1), "B")

        