# Title: Kth Smallest Element in a BST
# Runtime: 68 ms
# Memory: 17.9 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def inOrder(self, root: TreeNode, lst: List[int]) -> None:
        if not root:
            return
        self.inOrder(root.left, lst)
        lst.append(root.val)
        self.inOrder(root.right, lst)
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        lst = []
        self.inOrder(root, lst)
        return lst[k - 1]