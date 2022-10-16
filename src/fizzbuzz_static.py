class FizzBuzzStatic(object):
    """
    Fizzbuzz returns 'Fizz' if number is divisable
    by 3, 'Buzz' if divisible by 5, 'FizzBuzz' if
    divisable by both 3 and 5, otherwise return
    the string representation of the number.

    >>> FizzBuzzStatic.fizz(1)
    '1'
    >>> FizzBuzzStatic.fizz(3)
    'Fizz'
    >>> FizzBuzzStatic.fizz(5)
    'Buzz'
    >>> FizzBuzzStatic.fizz(15)
    'FizzBuzz'
    """
    @staticmethod
    def fizz(num):
        if num % 15 == 0:
            return "FizzBuzz"
        if num % 5 == 0:
            return "Buzz"
        if num % 3 == 0:
            return "Fizz"
        return str(num)
    