class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) < 1 or len(s) > 15:
            return 0
        hashmap = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9,
                   "V": 5, "IV": 4, "I": 1}
        output = 0
        for i in hashmap:
            while s.startswith(i):
                output += hashmap[i]
                s = s[len(i):]
        if output < 1 or output > 3999:
            return 0
        return output


if __name__ == '__main__':
    str = "LVIII"
    S = Solution()
    s2 = S.romanToInt(str)
    print(s2)
