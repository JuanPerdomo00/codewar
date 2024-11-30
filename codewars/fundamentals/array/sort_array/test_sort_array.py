import unittest
from main import is_odd, is_ord, sort_array


class Test(unittest.TestCase):
    def test_is_ord(self):
        self.assertEqual(is_ord(1), False)
        self.assertEqual(is_ord(2), True)
        self.assertEqual(is_ord(3), False)
        self.assertEqual(is_ord(4), True)

    def test_is_odd(self):
        self.assertEqual(is_odd(1), True)
        self.assertEqual(is_odd(2), False)
        self.assertEqual(is_odd(3), True)
        self.assertEqual(is_odd(4), False)

    def test_sort_array(self):
        self.assertEqual(sort_array([]), [])
        self.assertEqual(sort_array([5, 3, 2, 8, 1, 4, 11]), [1, 3, 2, 8, 5, 4, 11])
        self.assertEqual(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])


if __name__ == "__main__":
    unittest.main()
