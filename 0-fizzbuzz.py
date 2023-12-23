#!/usr/bin/python3

import sys


def fizzbuzz(n):
    """
    Fizzbuzz:- is popular program problem, where we have to print the number from
     1 to n, but print:
     fizz: if the number is multiple of three 3 instead of 3
     buzz: if the number is multiple of 5 instead of 5
     fizzbuzz: if the number is multiple of both 3 and 5
    """
    if n < 1:
        return
    tmp_result = []
    for i in range(1, n+1):
        if i % 3 == 0:
            tmp_result.append("Fizz")
        elif i % 5 == 0:
            tmp_result.append("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            tmp_result.append("FizzBuzz")
        else:
            tmp_result.append(str(i))
    print(" ".join(tmp_result))


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: /0-fizzbuzz.py <number>")
        print("Example: /0-fizzbuzz.py 89")
        sys.exit(1)
    number = int(sys.argv[1])
    fizzbuzz(50)