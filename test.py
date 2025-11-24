import pytest
from lesson_testing import (
    square_eq_solver,
    is_palindrome_iterative,
    compute_factorial
)

def test_square_eq_solver():
    assert (square_eq_solver(1, -3, 2) == [2.0, 1.0]
            or square_eq_solver(1, -3, 2) == [1.0, 2.0])
    assert square_eq_solver(1, 2, 1) == [-1.0]
    assert square_eq_solver(0, 0, 0) == []

def test_is_palindrome_iterative():
    assert is_palindrome_iterative("madam") is True
    assert is_palindrome_iterative("hello") is False

def test_compute_factorial():
    assert compute_factorial(5) == 120
    assert compute_factorial(0) == 1
