# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo={}
        def generate(start,end):
            if start==end:
                return [None]
            trees=[]
            for k in range(start, end):
                if (start,k) in memo:
                    left_trees=memo[(start,k)]
                else:
                    left_trees=generate(start,k)
                    memo[(start,k)]=left_trees
                if (k+1,end) in memo:
                    right_trees=memo[(k+1,end)]
                else:
                    right_trees=generate(k+1,end)
                    memo[(k+1,end)]=right_trees
                    
                for left_tree in left_trees:
                    for right_tree in right_trees:
                        tree=TreeNode(k)
                        tree.left=left_tree
                        tree.right=right_tree
                        trees.append(tree)
            return trees
        Resultat=generate(1,n+1)
        return Resultat
                
