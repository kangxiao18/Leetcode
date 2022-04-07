from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def getLength(head: ListNode):
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        dummy = ListNode(0, head)
        length = getLength(head)
        cur = dummy
        for i in range(0, length - n):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next




if __name__ == '__main__':
    str = [1,2,3,4,5]
    S = Solution()
    s2 = S.removeNthFromEnd(str, 2)
    print(s2)
