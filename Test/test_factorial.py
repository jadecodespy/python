import pytest
from Code import Factorial

def test_factorial():
    assert Factorial._factorial(6) == 720
