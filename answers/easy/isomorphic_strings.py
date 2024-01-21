def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    for i in range(0, len(s)):
        if s.index(s[i]) != t.index(t[i]):
            return False

    return True
