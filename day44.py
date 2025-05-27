import math

# Floor function
print(math.floor(2.3))  # Output: 2

# Square root * pi using alias
import math as m
result = m.sqrt(16) * m.pi
print(result)  # Output: 12.566370614359172

# Check available functions and constants in math
print(dir(math))  # Shows list of attributes

# Print nan constant and its type
print(math.nan, type(math.nan))  # Output: nan <class 'float'>

# Import custom module 'jim'
from jim import welcome, jim
import jim as ji

# Call imported function and variable
ji.welcome()
print(ji.jim)
print(welcome())
# Print __name__ attribute
print(__name__)  # Output: __main__ if run as script, module name if imported
# Print __doc__ attribute of math module            