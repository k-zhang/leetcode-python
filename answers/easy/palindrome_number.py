import sys


def is_palindrome(x):
    if x < 0:
        return False

    rev = 0
    y = x
    while y != 0:
        pop = y % 10
        y = y // 10

        if rev > sys.maxsize / 10 or (rev == sys.maxsize / 10 and pop > 7):
            return False

        rev = rev * 10 + pop

    return rev == x
