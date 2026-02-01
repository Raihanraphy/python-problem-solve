# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # dfs
        # bottom up postorder decision
        # return take/not take

        def dfs(node):
            if not node:
                return 0,0
            left_take, left_not = dfs(node.left)
            right_take,right_not = dfs(node.right)

            take     = node.val + left_not + right_not
            not_take = max(left_take, left_not) + max(right_take, right_not)

            return take, not_take

        return max(dfs(root))
