class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        result = []
        def _preorder(node):
            if not node:
                return
            result.append(node.val)  # Visit Root
            _preorder(node.left)     # Traverse Left
            _preorder(node.right)    # Traverse Right
        
        _preorder(root)
        return result
