class Solution:
    def isMatch(self, s, p):
        # Initialize DP table
        # Row indices represent the lengths of subpatterns
        # Col indices represent the lengths of substrings
        T = [
            [False for _ in range(len(s) + 1)]
            for _ in range(len(p) + 1)
        ]

        # Mark the origin as True, since p[:0] == "" and s[:0] == ""
        T[0][0] = True

        # Consider all subpatterns p[:i], i > 0 against empty string s[:0]
        for i in range(1, len(p) + 1):
            # Subpattern matches "" only if it consists of "{a-z}*" pairs
            T[i][0] = i > 1 and T[i - 2][0] and p[i - 1] == '*'

        # Consider the empty pattern p[:0] against all substrings s[:j], j > 0
        # Since an empty pattern cannot match non-empty strings, cells remain False

        # Match the remaining subpatterns (p[:i], i > 0) with the remaining
        # substrings (s[:j], j > 0)
        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):

                # Case 1: Last char of subpattern p[i-1] is an alphabet or '.'
                if p[i - 1] == s[j - 1] or p[i - 1] == '.':
                    T[i][j] |= T[i - 1][j - 1]

                # Case 2: Last char of subpattern p[i-1] is '*'
                elif p[i - 1] == '*':

                    # Case 2a: Subpattern doesn't need '*' to match the substring

                    # If the subpattern without '*' matches the substring,
                    # the subpattern with '*' must still match
                    T[i][j] |= T[i - 1][j]

                    # If the subpattern without '*' and its preceding alphabet
                    # matches the substring, then the subpattern with them
                    # must still match
                    T[i][j] |= i > 1 and T[i - 2][j]

                    # Case 2b: Subpattern needs '*' to match the substring

                    # If the alphabet preceding '*' matches the last char of
                    # the substring, then '*' is used to extend the match for
                    # the substring without its last char
                    if i > 1 and p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        T[i][j] |= T[i][j - 1]

        return T[-1][-1]

    def isMatch_2(self, s: str, p: str) -> bool:
        s, p = ' ' + s, ' ' + p
        lenS, lenP = len(s), len(p)
        dp = [[0] * (lenP) for i in range(lenS)]
        dp[0][0] = 1

        for j in range(1, lenP):
            if p[j] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, lenS):
            for j in range(1, lenP):
                if p[j] in {s[i], '.'}:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j] == "*":
                    dp[i][j] = dp[i][j - 2] or int(dp[i - 1][j] and p[j - 1] in {s[i], '.'})

        return bool(dp[-1][-1])

    cache = {}

    def isMatch_3(self, s, p):
        if (s, p) in self.cache:
            return self.cache[(s, p)]
        if not p:
            return not s
        if p[-1] == '*':
            if self.isMatch(s, p[:-2]):
                self.cache[(s, p)] = True
                return True
            if s and (s[-1] == p[-2] or p[-2] == '.') and self.isMatch_3(s[:-1], p):
                self.cache[(s, p)] = True
                return True
        if s and (p[-1] == s[-1] or p[-1] == '.') and self.isMatch_3(s[:-1], p[:-1]):
            self.cache[(s, p)] = True
            return True
        self.cache[(s, p)] = False
        return False

    def isMatch_4(self, s, p):
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        dp[0][0] = True
        for i in range(1, len(p)):
            dp[i + 1][0] = dp[i - 1][0] and p[i] == '*'
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == '*':
                    dp[i + 1][j + 1] = dp[i - 1][j + 1] or dp[i][j + 1]
                    if p[i - 1] == s[j] or p[i - 1] == '.':
                        dp[i + 1][j + 1] |= dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i][j] and (p[i] == s[j] or p[i] == '.')
        return dp[-1][-1]


if __name__ == '__main__':
    str = "aab"
    S = Solution()
    p = "c*a*b"
    s2 = S.isMatch(str, p)
    print(s2)