from app import add, hello, multiply, subtract, greet, hello_world, power, is_even, factorial

def test_hello():
    assert hello() == "Hello World"

def test_add():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(0, 0) == 0
    assert subtract(2, 5) == -3

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6

def test_greet():
    assert greet("World") == "Hello, World!"
    assert greet("Ahmet") == "Hello, Ahmet!"

def test_hello_world():
    assert hello_world() == "Hello, World!"

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1

def test_is_even():
    assert is_even(4) == True
    assert is_even(7) == False

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
