from typing import *


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n < 3:
            return 0
        if n == 3:
            return nums[0] + nums[1] + nums[2]
        nums.sort()
        closest = abs(nums[0] + nums[1] + nums[2] - target)
        output = nums[0] + nums[1] + nums[2]
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(s - target) < closest:
                    closest = abs(s - target)
                    output = s
                if s > target:
                    k0 = k - 1
                    while j < k0 and nums[k0] == nums[k]:
                        k0 -= 1
                    k = k0
                elif s < target:
                    j0 = j + 1
                    while j0 < k and nums[j] == nums[j0]:
                        j0 += 1
                    j = j0
                else:
                    return target
        return output


if __name__ == '__main__':
    str = [1, 1, 1, 1]
    target = 3
    S = Solution()
    s2 = S.threeSumClosest(str, target)
    print(s2)
