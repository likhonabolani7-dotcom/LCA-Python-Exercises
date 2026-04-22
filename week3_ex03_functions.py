def greet():
    print("Hello, World!")

def personalized_greeting(name):
    print(f"Hello, {name}")

def square(number):
    return number ** 2

result = square(5)
print(f"The square of 5 is {result}")

def rectangle_area(length, width):
    return length * width

area = rectangle_area(10, 5)
print(f"The area of the rectangle is {area}")

def double(number):
    return number * 2

def apply_operation(function, number):
    return function(number)

apply_double = apply_operation(double, 7)
print(f"Applying double to 7 gives {apply_double}")