from typing import List


def longest_palindrome(s: str) -> str:
    dp: List[List[bool]] = [[False for i in range(len(s))] for i in range(len(s))]

    max_length = 1
    start_index = 0

    for j in range(1, len(s)):
        for i in range(0, j+1):
            if s[i] != s[j]:
                dp[i][j] = False
            else:
                length = j - i + 1
                dp[i][j] = True if length <= 3 else dp[i+1][j-1]

                if dp[i][j] and length > max_length:
                    max_length = length
                    start_index = i

    return s[start_index:start_index + max_length]
