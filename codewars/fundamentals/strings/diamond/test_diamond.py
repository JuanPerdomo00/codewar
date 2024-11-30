import unittest
from main import diamod


class Test(unittest.TestCase):
    def test_check_num_positive(self):
        for num in range(1, 100):
            if num % 2 == 0 <= 0:
                self.assertEqual(diamod(num), None, f"Failed at num={num}")

    def test_check_num_negative(self):
        for num in range(-100, 0):
            if num % 2 == 0 <= 0:
                self.assertEqual(diamod(num), None, f"Failed at num={num}")

    def test_check_str(self):
        expected = " *\n"
        expected += "***\n"
        expected += " *\n"
        self.assertEqual(diamod(1), "*\n", "Failed :(")
        self.assertEqual(diamod(3), expected, "Failed :(")


if __name__ == "__main__":
    unittest.main()
