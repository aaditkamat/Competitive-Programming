# Title: Second Minimum Node In a Binary Tree
# Runtime: 32 ms
# Memory: 14 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def inOrder(self, root: TreeNode, lst: List[int]) -> int:
        if not root:
            return
        self.inOrder(root.left, lst)
        lst.append(root.val)
        self.inOrder(root.right, lst)
    
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        lst = []
        self.inOrder(root, lst)
        firstMinimum = min(lst)
        remaining = list(filter(lambda x: x != firstMinimum, lst))
        if not remaining:
            return -1
        return min(remaining)
        