import pytest
import math


def roots(a, b, c):
    if not all(isinstance(i, (int, float)) for i in [a, b, c]):
        return None

    D = b**2 - 4*a*c

    if D > 0:
       root1 = (-b + math.sqrt(D)) / (2*a)
       root2 = (-b - math.sqrt(D)) / (2*a)

       return min(root1, root2), max(root1, root2)
    elif D == 0:
        root = -b / (2*a)
        return root, root
    else:
        return None

def test_wrong_type_1():
    assert roots(None, 1, 1) is None


def test_wrong_type_2():
    assert roots(1, '1', 1) is None


def test_neg_discr():
    assert roots(1, 1, 1) is None


def test_equals_roots():
    root1, root2 = roots(1, 2, 1)
    assert root1 is not None and root1 == root2


def test_not_equals_roots_1():
    root1, root2 = roots(1, 3, -4)
    assert root1 is not None and root1 < root2


def test_not_equals_roots_2():
    root1, root2 = roots(1, 5, 3)
    assert root1 is not None and root1 < root2
