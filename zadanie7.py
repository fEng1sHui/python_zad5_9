from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*arg, **kwargs):
        print('Dekorator')
        return func(*arg,**kwargs)
    return wrapper

@my_decorator
def function():
    print('Hello world!')

def main():
    print(function.__name__)
    function()
if __name__ == '__main__':
    main()