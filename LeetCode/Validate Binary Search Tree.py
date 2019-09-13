# Title: Validate Binary Search Tree
# Runtime: 52 ms
# Memory: 16.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def postOrderTraverse(self, root: TreeNode, lst: List):
        if not root:
            return
        self.postOrderTraverse(root.left, lst)
        lst.append(root.val)
        self.postOrderTraverse(root.right, lst)
    
    def isSorted(self, lst: List) -> bool:
        for i in range(len(lst) - 1):
            if lst[i] >= lst[i + 1]:
                return False
        return True
        
    def isValidBST(self, root: TreeNode) -> bool:
        lst = []
        self.postOrderTraverse(root, lst)
        return self.isSorted(lst)
        
        