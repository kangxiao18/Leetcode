class Solution:
    def convert(self, s: str, numRows: int) -> str:
        L = [[] for i in range(numRows)]
        pos = 0
        direction = 1
        end = numRows -1
        if numRows > 1:
            for i in s:
                L[pos] += [i]
                if pos == 0:
                    direction = 1
                elif pos == end:
                    direction = -1
                pos += direction
            result = ""
            for i in range(len(L)):
                result += "".join(L[i])
            return result
        else:
            return s
        pass



if __name__ == '__main__':
    s = "PAYPALISHIRING"
    S = Solution()
    s2 = S.convert(s, 2)
    print(s2)