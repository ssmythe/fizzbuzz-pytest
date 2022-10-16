from src.fizzbuzz_static import FizzBuzzStatic
import pytest

def test_fizz_one():
    assert FizzBuzzStatic.fizz(1) == "1"

def test_fizz_three():
    assert FizzBuzzStatic.fizz(3) == "Fizz"

def test_fizz_five():
    assert FizzBuzzStatic.fizz(5) == "Buzz"

def test_fizz_three_and_five():
    assert FizzBuzzStatic.fizz(15) == "FizzBuzz"

def test_fizz_one_to_test():
    my_fizzes = []
    for i in range(1, 10+1):
        my_fizzes.append(FizzBuzzStatic.fizz(i))
    assert my_fizzes == [
        '1', '2', 'Fizz', '4', 'Buzz',
        'Fizz', '7', '8', 'Fizz', 'Buzz'
    ]
