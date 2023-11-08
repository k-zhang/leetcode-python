def length_of_longest_substring(s: str) -> int:
    ans = 0
    start = 0
    char_in_substring = {}

    for current in range(len(s)):
        if s[current] in char_in_substring:
            start = max(char_in_substring[s[current]], start)

        ans = max(ans, current - start + 1)
        char_in_substring[s[current]] = current + 1

    return ans
