# Title: Lowest Common Ancestor of a Binary Tree
# Runtime: 92 ms
# Memory: 27.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

TreeNodeInfo = collections.namedtuple('TreeNodeInfo', ['parent', 'level'])

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def dfsStoreInfo(self, root: TreeNodeInfo, mapping: dict):
        if not root.left and not root.right:
            return 
        if root.left:
            mapping[root.left.val] = TreeNodeInfo(root, mapping[root.val].level + 1)
            self.dfsStoreInfo(root.left, mapping)
        if root.right:
            mapping[root.right.val] = TreeNodeInfo(root, mapping[root.val].level + 1)
            self.dfsStoreInfo(root.right, mapping)
        return
            
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        mapping = {root.val: TreeNodeInfo(root, 0)}
        self.dfsStoreInfo(root, mapping)
        while p.val != q.val:
            pInfo, qInfo = mapping[p.val], mapping[q.val]
            if pInfo.level == qInfo.level:
                p, q = pInfo.parent, qInfo.parent
            elif pInfo.level > qInfo.level:
                p = pInfo.parent
            else:
                q = qInfo.parent
        return p
        
        
        