import pytest

from app import add, divide, greet, hello, multiply, subtract


class TestModuleSmoke:
    """Smoke tests to bring app.py to 100% line+branch coverage."""

    def test_hello(self):
        assert hello() == "Hello World"

    def test_add(self):
        assert add(1, 2) == 3

    def test_subtract(self):
        assert subtract(5, 2) == 3

    def test_multiply(self):
        assert multiply(3, 4) == 12

    def test_greet(self):
        assert greet("World") == "Hello, World!"


class TestDivide:
    def test_positive_integers(self):
        assert divide(10, 2) == 5

    def test_negative_dividend(self):
        assert divide(-10, 2) == -5

    def test_negative_divisor(self):
        assert divide(10, -2) == -5

    def test_both_negative(self):
        assert divide(-10, -2) == 5

    def test_float_result(self):
        assert divide(7, 2) == 3.5

    def test_floats(self):
        assert divide(1.5, 0.5) == 3.0

    def test_zero_dividend(self):
        assert divide(0, 5) == 0

    def test_one_as_divisor(self):
        assert divide(42, 1) == 42

    def test_division_by_zero_raises(self):
        with pytest.raises(ZeroDivisionError):
            divide(1, 0)

    def test_division_by_zero_zero_numerator_raises(self):
        with pytest.raises(ZeroDivisionError):
            divide(0, 0)
