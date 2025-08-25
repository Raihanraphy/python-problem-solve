# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
  def connect(self, root: 'Node | None') -> 'Node | None':
    if not root:
      return None

    def connectTwoNodes(p, q) -> None:
      if not p:
        return
      p.next = q
      connectTwoNodes(p.left, p.right)
      connectTwoNodes(q.left, q.right)
      connectTwoNodes(p.right, q.left)

    connectTwoNodes(root.left, root.right)
    return root
