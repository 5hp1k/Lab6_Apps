import pytest
import re


def is_under_queen_attack(position, queen_position):
    if not isinstance(position, str) or not isinstance(queen_position, str):
        raise TypeError("Both positions must be strings")

    if not re.match('^[a-h][1-8]$', position) or not re.match('^[a-h][1-8]$', queen_position):
        raise ValueError('Invalid chess coordinates')

    if position == queen_position:
        return True

    if position[0] == queen_position[0] or position[1] == queen_position[1]:
        return True

    if abs(ord(position[0]) - ord(queen_position[0])) == abs(ord(position[1]) - ord(queen_position[1])):
        return True

    return False


def test_wrong_type():
    with pytest.raises(TypeError):
        is_under_queen_attack(None, 42)


def test_wrong_coordinate():
    with pytest.raises(ValueError):
        is_under_queen_attack("abc", "42")


def test_wrong_coordinate2():
    with pytest.raises(ValueError):
        is_under_queen_attack('c3', 'd4d')


def test_wrong_coordinate_out_of_bounds():
    with pytest.raises(ValueError):
        is_under_queen_attack("e1", "e9")


def test_attack_same_field():
    assert is_under_queen_attack("e5", "e5")


def test_attack_same_row():
    assert is_under_queen_attack("a1", "e1")


def test_attack_same_column():
    assert is_under_queen_attack("a1", "a8")


def test_attack_diagonal():
    assert is_under_queen_attack("b3", "e6")


def test_no_attack():
    assert not is_under_queen_attack("c4", "e5")