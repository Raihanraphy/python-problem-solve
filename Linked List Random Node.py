# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from random import randint
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.l = []
        cur = head
        while cur:
            self.l.append(cur.val)
            cur = cur.next
        self.N = len(self.l)

    def getRandom(self) -> int:
        i = randint(0, self.N - 1)
        return self.l[i]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
