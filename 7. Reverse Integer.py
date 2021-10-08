class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s[0] == '-':
            s2 = s[1:]
            s2 = s2[::-1]
            non_zero_pos = 0
            for j in range(len(s2)):
                if s2[j] != '0':
                    non_zero_pos = j
                    break
            s2 = s2[non_zero_pos:]
            s = s[0] + s2
        else:
            s = s[::-1]
            non_zero_pos = 0
            for j in range(len(s)):
                if s[j] != '0':
                    non_zero_pos = j
                    break
            s = s[non_zero_pos:]
        s = int(s)
        if s < -pow(2, 31) or s > pow(2, 31) - 1:
            return 0
        else:
            return s
