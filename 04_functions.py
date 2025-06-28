# Functions : reusing your code

# Example 1: A simple function that prints a message
def greet(name):
  print("Hello, " + name + "!")

greet("MicroPython")

# Example 2: A function that adds two numbers and returns the result
def add_numbers(a, b):
  result = a + b
  return result

sum_result = add_numbers(10, 20)
print("Sum:", sum_result)

# Example 3: A function with a default argument
def power(base, exponent=2):
  result = base ** exponent
  return result

print("5 squared:", power(5))
print("2 cubed:", power(2, 3))

# Example 4: A function that checks if a number is even
def is_even(number):
  if number % 2 == 0:
    return True
  else:
    return False

print("Is 4 even?", is_even(4))
print("Is 7 even?", is_even(7))
