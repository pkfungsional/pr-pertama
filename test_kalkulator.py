import unittest

from kalkulator import kurang, tambah


class TestKalkulator(unittest.TestCase):
    def test_tambah(self):
        self.assertEqual(tambah(2, 3), 5)

    def test_kurang(self):
        self.assertEqual(kurang(5, 3), 2)
        self.assertEqual(kurang(3, 5), -2)


if __name__ == "__main__":
    unittest.main()
