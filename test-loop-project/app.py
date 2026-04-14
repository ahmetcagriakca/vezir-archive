def hello():
    return "Hello World"

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def greet(name):
    return f"Hello, {name}!"

def divide(a, b):
    return a / b

def hello_world():
    return "Hello, World!"

def power(a, b):
    return a ** b

def is_even(n):
    return n % 2 == 0

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def max_of_three(a, b, c):
    return max(a, b, c)
