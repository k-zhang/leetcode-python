def is_armstrong(n):
    s = str(n)
    power = len(s)

    total = 0
    for i in range(0, power):
        total += pow(int(s[i:i + 1]), power)

    return total == n
