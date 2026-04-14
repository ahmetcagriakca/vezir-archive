def cube(n):
    return n * n * n


def test_cube_two():
    assert cube(2) == 8


def test_cube_three():
    assert cube(3) == 27


def test_cube_zero():
    assert cube(0) == 0


def test_cube_negative_two():
    assert cube(-2) == -8
