# Title: Lowest Common Ancestor of a Binary Search Tree
# Runtime: 104 ms
# Memory: 18.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Similar to Q236

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:            
    def getParentDFS(self, root: TreeNode, mapping: dict):
        if not root.left and not root.right:
            return
        if root.left:
            mapping[root.left] = root
            self.getParentDFS(root.left, mapping)
        if root.right:
            mapping[root.right] = root
            self.getParentDFS(root.right, mapping)
            
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        mapping = {}
        self.getParentDFS(root, mapping)
        while True:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
                
                
        