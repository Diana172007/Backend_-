"""Тесты для модуля calculator."""

import unittest

from z_3 import add_numbers


class TestAddNumbers(unittest.TestCase):
    """Тесты функции add_numbers."""

    def test_positive_numbers(self) -> None:
        """Сложение двух положительных чисел."""
        self.assertEqual(add_numbers(2, 3), 5)


if __name__ == "__main__":
    unittest.main()
