class Solution:
    def maximumProduct3(self, nums) -> int:
        max_product = float("-inf")
        for i in range(len(nums)):
            if len(nums) > i+2:
                pos_j = i + 1
                for j in nums[i+1:]:
                    pos_k = pos_j + 1
                    for k in nums[pos_j+1:]:
                        p = nums[i]*j*k
                        if max_product < p:
                            max_product = p
                        pos_k += 1
                    pos_j += 1
        return max_product

    def maximumProduct2(self, nums) -> int:
        '''
        最终结果的组成：
        1、if 3正或者3负，则都是直接取nums中最大的三个数 max1*max2*max3
        2、if 2正1负，则正数则肯定只有两个，那么负数一定越大越好，则还是取nums中最大的三个数，与1公式相同
        3、if 1正2负，则负数最小的两个值的乘积 > 组内最大两个数的乘积 min1*min2*max1
        所以公式为max(1,3)，一、三两种情况的最大值。
        '''
        nums = sorted(nums, reverse=True)
        return max(nums[0]*nums[1]*nums[2], nums[0]*nums[-1]*nums[-2])

    # Best Anwser
    def maximumProduct(self, nums) -> int:
        # 最小的和第二小的
        min1 = float("inf")
        min2 = float("inf")
        # 最大的、第二大的和第三大的
        max1 = float("-inf")
        max2 = float("-inf")
        max3 = float("-inf")

        for x in nums:
            if x < min1:
                min2 = min1
                min1 = x
            elif x < min2:
                min2 = x

            if x > max1:
                max3 = max2
                max2 = max1
                max1 = x
            elif x > max2:
                max3 = max2
                max2 = x
            elif x > max3:
                max3 = x
        return max(min1 * min2 * max1, max1 * max2 * max3)

if __name__ == '__main__':
    x = [2, 1,-2,-3]
    S = Solution()
    y = S.maximumProduct(x)
    print(y)