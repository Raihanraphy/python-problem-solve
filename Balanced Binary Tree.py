class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0

            left = height(node.left)
            if left == -1:  # left subtree unbalanced
                return -1

            right = height(node.right)
            if right == -1:  # right subtree unbalanced
                return -1

            if abs(left - right) > 1:
                return -1  # current node unbalanced

            return max(left, right) + 1  # return height if balanced

        return height(root) != -1
