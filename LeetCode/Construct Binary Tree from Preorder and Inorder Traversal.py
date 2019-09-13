# Title: Construct Binary Tree from Preorder and Inorder Traversal
# Runtime: 68 ms
# Memory: 18.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def getMapping(self, inorder: List[int]) -> dict:
        mapping = {}
        for index in range(len(inorder)):
            num = inorder[index]
            mapping[num] = index
        return mapping
    
    def buildTreeRecursive(self, preorder: List[int], mapping: dict, left: int, right: int) -> TreeNode:
        if right < left:
            return None
        num = preorder.pop(0)
        curr = TreeNode(num)
        curr.left = self.buildTreeRecursive(preorder, mapping, left, mapping[num] - 1)
        curr.right = self.buildTreeRecursive(preorder, mapping, mapping[num] + 1, right)
        return curr
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not len(preorder) == len(inorder):
            return None
        mapping = self.getMapping(inorder)
        return self.buildTreeRecursive(preorder, mapping, 0, len(inorder) - 1)
            
        