class Solution:
    def maxArea(self, height):
        if len(height) < 2 or len(height) > pow(10, 5) or min(height) < 0 or max(height) > pow(10, 4):
            return 0
        tank = 0
        num_count = 0
        min_num = 0
        for i in range(len(height) - 1):
            if min_num < height[i]:
                min_num = height[i]
            k = i + 1
            for j in range(len(height) - i - 1):

                min_num = height[i]
                num_count = k - i
                if min_num > height[k]:
                    min_num = height[k]
                if tank < min_num * num_count:
                    tank = min_num * num_count
                k += 1
        return tank


if __name__ == '__main__':
    str = [1, 2, 1]
    S = Solution()
    s2 = S.maxArea(str)
    print(s2)
