class FizzBuzz():
    """
    Fizzbuzz returns 'Fizz' if number is divisable
    by 3, 'Buzz' if divisible by 5, 'FizzBuzz' if
    divisable by both 3 and 5, otherwise return
    the string representation of the number.

    >>> fb=FizzBuzz()
    >>> fb.fizz(1)
    '1'
    >>> fb.fizz(3)
    'Fizz'
    >>> fb.fizz(5)
    'Buzz'
    >>> fb.fizz(15)
    'FizzBuzz'
    """
    def fizz(self, num):
        if num % 15 == 0:
            return "FizzBuzz"
        if num % 5 == 0:
            return "Buzz"
        if num % 3 == 0:
            return "Fizz"
        return str(num)
    