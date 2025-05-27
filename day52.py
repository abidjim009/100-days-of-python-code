#def double(x):
 #   return x * 2

def appl(fx, value):
    return 6 + fx(value)

double = lambda x: x * 2
# Example usage

cube = lambda x: x ** 3
# Example usage

average = lambda x, y: (x + y) / 2
# Example usage
print(average(10, 20 ))  
print(cube(3))  # Output: 27
print(double(5))  # Output: 10
print(appl(double, 5))  # Output: 16