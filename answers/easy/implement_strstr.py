def strstr(haystack, needle):
    if needle == '':
        return 0
    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            if haystack[i:i + len(needle)] == needle:
                return i
    return -1
