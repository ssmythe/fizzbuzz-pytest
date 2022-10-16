from src.fizzbuzz import FizzBuzz
import pytest

@pytest.fixture
def fb():
    return FizzBuzz()

def test_fizz_one(fb):
    assert fb.fizz(1) == "1"

def test_fizz_three(fb):
    assert fb.fizz(3) == "Fizz"

def test_fizz_five(fb):
    assert fb.fizz(5) == "Buzz"

def test_fizz_three_and_five(fb):
    assert fb.fizz(15) == "FizzBuzz"

def test_fizz_one_to_test(fb):
    my_fizzes = []
    for i in range(1, 10+1):
        my_fizzes.append(fb.fizz(i))
    assert my_fizzes == [
        '1', '2', 'Fizz', '4', 'Buzz',
        'Fizz', '7', '8', 'Fizz', 'Buzz'
    ]
