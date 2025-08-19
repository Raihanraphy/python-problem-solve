import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        result = []
        if not root:
            return result

        queue = collections.deque([root])
        left_to_right = True

        while queue:
            level_size = len(queue)
            current_level_nodes = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if not left_to_right:
                current_level_nodes.reverse()

            result.append(current_level_nodes)
            left_to_right = not left_to_right

        return result
