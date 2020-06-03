import pytest
from Code import generator

def test_dict_generator():
    assert generator.dict_generator(2) == {1: 1, 2: 4}