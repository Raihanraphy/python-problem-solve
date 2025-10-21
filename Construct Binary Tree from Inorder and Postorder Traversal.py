class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx = len(postorder) - 1
        inorderMap = {}

        def build(left: int, right: int) -> Optional[TreeNode]:
            nonlocal idx

            if left > right:
                return None

            node = TreeNode(postorder[idx])

            idx -= 1

            node.right = build(inorderMap[node.val]+1, right)
            node.left = build(left, inorderMap[node.val]-1)

            return node

        for i in range(len(inorder)):
            inorderMap[inorder[i]] = i

        return build(0, len(postorder) - 1)
