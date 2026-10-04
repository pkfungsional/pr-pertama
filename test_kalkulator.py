import unittest

from kalkulator import tambah


class TestKalkulator(unittest.TestCase):
    def test_tambah(self):
        self.assertEqual(tambah(2, 3), 5)


if __name__ == "__main__":
    unittest.main()
