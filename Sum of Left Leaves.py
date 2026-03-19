from collections import deque

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        s = 0
        q = deque()
        q.append((root, 'R'))  

        while q:
            node, lr = q.popleft()

            if lr == 'L' and not node.left and not node.right:
                s += node.val

            if node.left:
                q.append((node.left, 'L'))
            if node.right:
                q.append((node.right, 'R'))

        return s
            
        
