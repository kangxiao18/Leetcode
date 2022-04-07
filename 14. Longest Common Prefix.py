class Solution:
    def longestCommonPrefix(self, strs):
        minLen = min(len(s) for s in strs)
        str = strs[0]
        common = ""
        flag = True
        for i in range(minLen):
            for j in strs:
                if str[i] != j[i]:
                    flag = False
                    break
            if flag:
                common += str[i]
            else:
                break
        return common


if __name__ == '__main__':
    str = ["dog","racecar","car"]
    S = Solution()
    s2 = S.longestCommonPrefix(str)
    print(s2)
