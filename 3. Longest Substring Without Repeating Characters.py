class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        for j in range(len(s)):
            sub_s = s[j:]
            if (len(sub_s) < max_count) and len(sub_s) != 0:
                return max_count
            temp_set = set()
            for i in sub_s:
                if i not in temp_set:
                    temp_set.add(i)
                else:
                    break
            temp_count = len(temp_set)
            if max_count < temp_count:
                max_count = temp_count
        return max_count


if __name__ == '__main__':
    s = " "

    S = Solution()
    num = S.lengthOfLongestSubstring(s)
    print(num)
