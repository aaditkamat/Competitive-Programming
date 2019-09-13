# Title: Subtree of Another Tree
# Runtime: 180 ms
# Memory: 14.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sameTree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
    
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        if self.isSubtree(s.left, t) or self.isSubtree(s.right, t):
            return True
        return self.sameTree(s, t)
        