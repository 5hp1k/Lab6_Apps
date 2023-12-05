import pytest
from collections import Counter


def count_chars(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return dict(Counter(s))


def test_wrong_type():
    with pytest.raises(TypeError):
        count_chars(42)


def test_empty():
    counts = count_chars('')
    assert counts == {}


def test_common():
    counts = count_chars('aabccc')
    assert counts == {'a': 2, 'b': 1, 'c': 3}