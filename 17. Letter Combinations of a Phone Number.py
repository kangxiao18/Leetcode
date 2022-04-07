from typing import *


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        letter_dict = {"2": ["a", 'b', 'c'], "3": ["d", 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                       '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        combination = list()
        combinations = list()

        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in letter_dict[digit]:
                    combination.append(letter)
                    backtrack(index+1)
                    combination.pop()
        backtrack(0)
        return combinations

    def letterCombinations2(self, digits: str) -> List[str]:
        if not digits: return []

        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(conbination, nextdigit):
            if len(nextdigit) == 0:
                res.append(conbination)
            else:
                for letter in phone[nextdigit[0]]:
                    backtrack(conbination + letter, nextdigit[1:])

        res = []
        backtrack('', digits)
        return res



if __name__ == '__main__':
    str = "2332"
    S = Solution()
    s2 = S.letterCombinations(str)
    print(s2)
