def plus_one(digits):
    for i in range(len(digits)-1, -1, -1):
        if digits[i] + 1 < 10:
            digits[i] += 1
            break
        else:
            digits[i] = 0

    if digits[0] == 0:
        new_digits = [0 for _ in range(len(digits) + 1)]
        new_digits[0] = 1
        digits = new_digits

    return digits
