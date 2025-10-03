from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root: Optional[TreeNode], lst: List[int]):
            if root is None:
                return
            helper(root.left, lst)
            helper(root.right, lst)
            lst.append(root.val)
        
        result = []
        helper(root, result)
        return result
