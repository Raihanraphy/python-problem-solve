# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        dummy_node = ListNode(-1, head)
      
        
        previous = dummy_node
      
        
        while previous.next:
            
            if previous.next.val != val:
                
                previous = previous.next
            else:
                
                previous.next = previous.next.next
      
        
        return dummy_node.next
        
