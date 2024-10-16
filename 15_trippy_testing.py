"""
Exercise 1: Divide
"""
def divide(a, b):
  """Divides two numbers, handling potential division by zero.

  Args:
    a: The numerator.
    b: The denominator.

  Returns:
    The quotient, or None if b is zero.
  """

  if b == 0:
    return None
  else:
    return a / b


assert divide(35/7) == 5 #Divides 35 by 7 to get 5 
assert divide(80/10) == 10 #Divides 80 by 10 to get 10


Exercise 2: Factorial

def factorial(n):
  """Calculates the factorial of a non-negative integer.

  Args:
    n: A non-negative integer.

  Returns:
    The factorial of n.
  """

  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)


assert factorial(0) == 0 #Checks for two factorials for 0 and 5
assert factorial(5) == 120

"""
Exercise 3: String Reverse

def reverse_string(string):
  """Reverses a given string.

  Args:
    string: A string to be reversed.

  Returns:
    """The reversed string.


  reversed_string = ""
  for char in string:
    reversed_string = char + reversed_string
  return reversed_string


assert reverse_string("California Love Party") == "ytrap evoL ainrofilaC" #Reverses the string backwards for both asserts
assert reverse_string("Katie is a runner") == "rennur a si eitaK"

Exercise 4: Fibonacci
"""
    def fibonacci(n):
        """Generates the nth Fibonacci number.

    Args:
        n: The index of the Fibonacci number to calculate.

  Returns:
    The nth Fibonacci number.

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


assert fibonacci(0) == 0 #Fibonacci sequences of 0,1 and 19
assert fibonacci(1) == 1
assert fibonacci(19) == 4181
"""

Exercise  5: Email Validation


import re

def is_valid_email(email):
  """Determines whether email is valid or not

  Args:
    email: The email to validate

  Returns:
    Boolean value if email is valid
  """
  email_regex = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+"
  return re.match(email_regex, email) is not None

assert is_valid_email("cookiecrumb21@gmail.com") == True #Makes a real email and a fake email
assert is_valid_email("georgepicks@hotcakes.com") == False

