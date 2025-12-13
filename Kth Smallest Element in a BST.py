# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        found,answer=self.count_nodes(root,k)
        return answer

    def count_nodes(self,root,rem_k):
        found=False
        if root.left is not None:
            found,rem_k=self.count_nodes(root.left,rem_k)
            if found:
                return True,rem_k
        rem_k-=1
        if (rem_k)==0:
            return True,root.val
        else:
            if root.right is not None:
                found,rem_k=self.count_nodes(root.right,rem_k)
                if found:
                    return True,rem_k
            return False,rem_k
        return False,-1
    
            



    
