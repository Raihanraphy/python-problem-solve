class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        current = root
        while current:
            if current.left:
                # Find the rightmost node in the left subtree
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right
                
                # Connect the rightmost node to the current node's right child
                predecessor.right = current.right
                
                # Move the left subtree to the right
                current.right = current.left
                
                # Nullify the left child
                current.left = None
            
            # Move to the next node in the flattened list
            current = current.right
