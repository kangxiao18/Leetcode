class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) > 0:
            if s[0] == '-' or s[0] == '+':
                if len(s) > 1:
                    if not s[1].isdigit():
                        return 0
                    else:
                        return self.calculate_result(s)
            elif s[0].isdigit():
                return self.calculate_result(s)
            else:
                return 0
        return 0

    def calculate_result(self, s: str) -> int:
        sr = ""
        for i in s[1:]:
            if i.isdigit():
                sr += i
            else:
                break
        sr = s[0] + sr
        num_sr = int(sr)
        if num_sr < -pow(2, 31):
            num_sr = -pow(2, 31)
        elif num_sr > pow(2, 31) - 1:
            num_sr = pow(2, 31) - 1
        return num_sr


if __name__ == '__main__':
    str = "-91283472332"
    S = Solution()
    s2 = S.myAtoi(str)
    print(s2)
