#!Zaimplementuj dekorator, który zliczy i wypisze na standardowe wyjście liczbę wywołań danej funkcji,
import functools

def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls

@count_calls
def say_whee():
    print("Whee!")

def main():
    say_whee()
    say_whee()
    say_whee()
    print(f"Call {say_whee.num_calls}")

if __name__ == '__main__':
    main()