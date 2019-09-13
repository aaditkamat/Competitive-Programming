# Title: Symmetric Tree
# Runtime: 112 ms
# Memory: 14.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def swap_trees(self, root: TreeNode) -> TreeNode:
        temp = root.left
        root.left = root.right
        root.right = temp
        return root
        
    def rotate(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        root = self.swap_trees(root)
        root.left = self.rotate(root.left)
        root.right = self.rotate(root.right)
        return root
    
    def are_equal_trees(self, rotated_root: TreeNode, root: TreeNode) -> bool:
        if not rotated_root and not root:
            return True
        if not rotated_root or not root:
            return False
        print(root, rotated_root)
        return root.val == rotated_root.val and self.are_equal_trees(rotated_root.left, root.left) and self.are_equal_trees(rotated_root.right, root.right)
    
    def isSymmetric(self, root: TreeNode) -> bool:
        rotated_root = self.rotate(copy.deepcopy(root))
        return self.are_equal_trees(rotated_root, root)