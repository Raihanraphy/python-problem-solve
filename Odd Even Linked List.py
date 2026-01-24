# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Handle empty list
        if head is None:
            return None
      
        # Initialize pointers for odd and even lists
        odd_current = head                    # Pointer to traverse odd nodes
        even_head = head.next                 # Store the head of even list for later connection
        even_current = head.next              # Pointer to traverse even nodes
      
        # Traverse the list and separate odd and even nodes
        while even_current and even_current.next:
            # Connect current odd node to next odd node
            odd_current.next = even_current.next
            odd_current = odd_current.next
          
            # Connect current even node to next even node
            even_current.next = odd_current.next
            even_current = even_current.next
      
        # Connect the end of odd list to the head of even list
        odd_current.next = even_head
      
        return head
