# Title: Balanced Binary Tree
# Runtime: 80 ms
# Memory: 18.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def height(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
    
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        if abs(leftHeight - rightHeight) >= 2:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)