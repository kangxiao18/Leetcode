class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        n = len(nums3)
        if n == 0:
            return 0
        elif n == 1:
            return nums3[0]
        else:
            if n % 2 == 1:
                return nums3[n//2]
            else:
                return (nums3[n//2-1] + nums3[n//2])/2


if __name__ == '__main__':
    S = Solution()
    nums1 = []
    nums2 = []
    r = S.findMedianSortedArrays(nums1, nums2)
    print(r)