# Title: Invert Binary Tree
# Runtime: 40 ms
# Memory: 13.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        temp = root.left
        root.left = root.right
        root.right = temp
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        return root