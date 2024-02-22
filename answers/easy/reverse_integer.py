def reverse_integer(x):
    rev = 0
    while x != 0:
        pop = x % 10
        x = x // 10
        rev = rev * 10 + pop
    return rev
