# Title: Range Sum of BST
# Runtime: 604 ms
# Memory: 24.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        sum = 0
        if root == None:
            return 0
        if root.val in range(L, R + 1):
            sum = root.val
        return sum + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
        