from app import multiply, greet

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6

def test_greet():
    assert greet("World") == "Hello, World!"
    assert greet("Ahmet") == "Hello, Ahmet!"
