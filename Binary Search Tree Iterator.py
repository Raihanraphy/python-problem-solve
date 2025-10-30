# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self,root):
        self.sorted_nodes = []
        self.index = - 1
        self._inorder(root)
    
    def _inorder(self,root):
        if root is None:
            return
        
        self._inorder(root.left)
        self.sorted_nodes.append(root.val)
        self._inorder(root.right)


    def next(self):
        self.index += 1
        return self.sorted_nodes[self.index]

    def hasNext(self):
        return self.index < len(self.sorted_nodes) - 1






# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
