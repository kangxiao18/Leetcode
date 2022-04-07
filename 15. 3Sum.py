from typing import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        n = len(nums)
        if n < 3:
            return output
        for first in range(n):
            if nums[first] > 0:
                break
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            L = first + 1
            R = n - 1
            while L < R:
                if nums[first] + nums[L] + nums[R] > 0:
                    R -= 1
                elif nums[first] + nums[L] + nums[R] < 0:
                    L += 1
                else:
                    output.append([nums[first], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L+1]:
                        L += 1
                    while L < R and nums[L] == nums[R-1]:
                        R -= 1
                    L += 1
                    R -= 1
        return output


if __name__ == '__main__':
    str = [-1, 0, 1, 2, -1, -4]
    S = Solution()
    s2 = S.threeSum(str)
    print(s2)
