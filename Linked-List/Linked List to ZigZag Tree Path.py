# binarysearch.com weekly coding 2
class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        if node is None:
            return None
        root = Tree(node.val)
        if node.next:
            if node.next.val < node.val:
                root.left = self.solve(node.next)
            else:
                root.right = self.solve(node.next)
        return root

