# The isMatch method checks if `s` matches `p` with wildcard characters '?' and '*'.

# Recursive Approach:
# - '?' matches any single character.
# - '*' matches any sequence (including an empty sequence).
# - Recursively check:
#   - If characters match or '?' is found, move both indices back.
#   - If '*', try ignoring it or matching it with a character.
#   - If one string is exhausted, check if only '*' remains in `p`.

# TC: O(2^n) - Exponential due to recursion.
# SC: O(n) - Recursion stack space.


class Solution:
    def solve(self, index1, index2, text, pattern):
        if index1 < 0 and index2 < 0:
            return True
        if index2 < 0 and index1 >= 0:
            return False
        if index1 < 0 and index2 >= 0:
            for i in range(index2 + 1):
                if pattern[i] != '*':
                    return False
            return True

        if text[index1] == pattern[index2] or pattern[index2] == '?':
            return self.solve(index1 - 1, index2 - 1, text, pattern)

        if pattern[index2] == '*':
            return self.solve(index1 - 1, index2, text, pattern) or self.solve(index1, index2 - 1, text, pattern)

        return False

    def isMatch(self, s: str, p: str) -> bool:
        n1 = len(s)
        n2 = len(p)
        return self.solve(n1 - 1, n2 - 1, s, p)