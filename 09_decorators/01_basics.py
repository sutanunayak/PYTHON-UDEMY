from functools import wraps

def my_decorators(func):
    @wraps(func)
    def wrapper():
        print("Before the function call.")
        func()
        print("After the function call.")
    return wrapper

@my_decorators
def greet():
    print("Hello from decorators class from this")

greet()
print(greet.__name__)