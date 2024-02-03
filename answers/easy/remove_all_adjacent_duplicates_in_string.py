def remove_all_adjacent_duplicates_in_string(s):
    result = []
    for c in s:
        if len(result) != 0 and result[-1] == c:
            result.pop()
        else:
            result.append(c)
    return "".join(result)
