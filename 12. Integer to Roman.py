class Solution:
    def intToRoman(self, num: int) -> str:
        # 1 <= num <= 3999
        if num < 1 or num > 3999:
            return ""
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num // 1000] + C[num % 1000 // 100] + X[num % 100 // 10] + I[num % 10]

    def intToRoman2(self, num: int) -> str:
        # 1 <= num <= 3999
        if num < 1 or num > 3999:
            return ""
        hashmap = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX",
                   5: "V", 4: "IV", 1: "I"}
        output = ""
        for i in hashmap:
            n = num // i
            output += n * hashmap[i]
            num -= n * i
        return output


if __name__ == '__main__':
    str = 3
    S = Solution()
    s2 = S.intToRoman(str)
    print(s2)
    s2 = S.intToRoman2(str)
    print(s2)
