# Decorators with functions
# Decorators are a way to modify or enhance functions or methods without changing their actual code.
def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx()
        print("Thanks for using this function")
    return mfx

@greet

def hello():
    print("Hello, how are you?")


    @greet
    def add(x, y):
        print(x + y)

        hello()
        greet(add)(1,2)

import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b