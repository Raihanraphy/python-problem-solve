# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        q = [(root, str(root.val))]

        while q:
            node, path = q.pop()
            if not node.right and not node.left:
                res.append(path)
            
            if node.left:
                q.append((node.left, str(path) + "->" + str(node.left.val)))
            if node.right:
                q.append((node.right, str(path) + "->" + str(node.right.val)))
        return res
        
