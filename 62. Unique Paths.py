from typing import *
import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        print(arr)
        for i in range(1, m):
            for j in range(1, n):
                arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
        return arr[m - 1][n - 1]

    def uniquePaths2(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, n - 1)

if __name__ == '__main__':
    str = "472332"
    S = Solution()
    s2 = S.uniquePaths2(3, 7)
    print(s2)
