
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val=[]
        while head:
            val.append(head.val)
            head=head.next
        
        val.sort()

        dummy=current=ListNode()
        for v in val:
            current.next=ListNode(v)
            current=current.next
        return dummy.next
        
