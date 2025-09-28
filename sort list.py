# Definition for singly-linked list.
# class ListNode:
# def __init__(self, val=0, next=None):
# self.val = val
# self.next = next

import random

class Solution:
    def __init__(self):
        self.len = 0

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        lst=[]
        while temp:
            lst.append(temp.val)
            temp=temp=temp.next

        lst.sort()
        temp=head
        for i in lst:
            temp.val=i
            temp=temp.next

        return head    
        
    def partition(self, head, tail, length): 
        rand_pivot = self.getMiddle(head, tail, length)


        rand_pivot.val, head.val = head.val, rand_pivot.val

        pivot = head
        pre = head
        curr = head
        
        while curr:
            if curr.val < pivot.val:
                pre.next.val, curr.val = curr.val, pre.next.val
                pre = pre.next
            curr = curr.next

        pivot.val, pre.val = pre.val, pivot.val
        return pre 
