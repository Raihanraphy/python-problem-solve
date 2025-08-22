# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.current_sum = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        """
        Determines if the tree has a root-to-leaf path such that
        adding up all the values along the path equals the given sum.

        :param root: TreeNode, the root of the binary tree
        :param target_sum: int, the target sum to be achieved
        :return: bool, True if such a path exists, False otherwise
        """
      
        def dfs(node, current_sum):
            """
            Depth-first search helper function that traverses the tree
            to find a root-to-leaf path that sums to the target_sum.

            :param node: TreeNode, the current node being traversed
            :param current_sum: int, the sum of the values from the root node up to the current node
            :return: bool, True if a path is found, False otherwise
            """
            if node is None:
                # Base case: if the current node is None, no path exists
                return False
          
            # Update the current_sum by adding the current node's value
            current_sum += node.val
          
            # Check if the current node is a leaf and matches the target_sum
            if node.left is None and node.right is None and current_sum == target_sum:
                return True
          
            # Recursively search in the left and right subtrees for the path
            # If either subtree returns True, a valid path has been found
            return dfs(node.left, current_sum) or dfs(node.right, current_sum)

        # Start DFS traversal from the root with an initial sum of 0
        return dfs(root, 0)
