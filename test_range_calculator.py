import unittest

from range_calculator import calculate_range


class RangeCalculatorTests(unittest.TestCase):
    def test_inclusive_range(self):
        self.assertEqual(
            calculate_range(1, 5),
            {"count": 5, "total": 15, "span": 4},
        )

    def test_exclusive_range(self):
        self.assertEqual(
            calculate_range(1, 5, inclusive=False),
            {"count": 4, "total": 10, "span": 4},
        )

    def test_reversed_inputs(self):
        self.assertEqual(
            calculate_range(8, 3),
            {"count": 6, "total": 33, "span": 5},
        )


if __name__ == "__main__":
    unittest.main()
