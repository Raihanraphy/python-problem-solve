# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node,mini,maxi):
            if not node:
                return True
            if not (node.val<maxi and node.val>mini):
                return False
            return valid(node.left,mini,node.val) and valid(node.right,node.val,maxi)
        return valid(root,float('-inf'),float('inf'))
