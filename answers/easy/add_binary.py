def add_binary(a, b):
    n = len(a)
    m = len(b)
    if n < m:
        return add_binary(b, a)
    L = max(n, m)

    carry = 0
    j = m - 1

    sb = []
    for i in range(L - 1, -1, -1):
        if a[i] == '1':
            carry += 1
        if j > -1 and b[j] == '1':
            carry += 1
        j -= 1

        if carry % 2 == 1:
            sb.append('1')
        else:
            sb.append('0')

        carry //= 2

    if carry == 1:
        sb.append('1')

    sb.reverse()

    return "".join(sb)
