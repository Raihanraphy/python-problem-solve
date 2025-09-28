python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        output = 0

        def recursive(node, currSum):
            nonlocal output
            if not node:
                return
            
            if not node.left and not node.right:
                output += currSum * 10 + node.val

            recursive(node.left, currSum * 10 + node.val)
            recursive(node.right, currSum * 10 + node.val)
        
        recursive(root, 0)
        return output
