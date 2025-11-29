# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def treeHeight(root: Optional[TreeNode]) -> int:
            count = 0
            while root:
                count += 1
                root = root.left
            return count
        
        if not root:
            return 0
        left_h = treeHeight(root.left)
        right_h = treeHeight(root.right)

        if left_h == right_h:
            return 1 + (2**left_h-1) + self.countNodes(root.right)
        else:
            return 1 + self.countNodes(root.left) + (2**(right_h)-1)
