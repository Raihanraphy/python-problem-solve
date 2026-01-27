# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first,self.middle,self.last=None,None,None
        self.prev=TreeNode(float('-inf'))
        self.inorder(root)
        if self.last and self.middle:
            self.first.val,self.last.val=self.last.val,self.first.val
        elif self.first and self.middle:
            self.first.val,self.middle.val=self.middle.val,self.first.val

    def inorder(self,root):
        if root==None:
            return
        self.inorder(root.left)
        if self.prev and root.val<self.prev.val:
            if self.first==None:
                self.first=self.prev
                self.middle=root
            else:
                self.last=root
        self.prev=root
        self.inorder(root.right)
