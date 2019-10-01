# Title: Remove Duplicates from Sorted List II
# Runtime: 48 ms
# Memory: 13.9 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def getMapping(self, head:ListNode) -> dict:
        mapping = {}
        curr = head
        while curr:
            if curr.val in mapping:
                mapping[curr.val] += 1
            else:
                mapping[curr.val] = 1
            curr = curr.next
        return mapping
            
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        mapping = self.getMapping(head)
        currNode, nextNode = head, head.next
        while nextNode:
            if mapping[nextNode.val] > 1:
                 currNode.next = nextNode.next
            else:
                 currNode = nextNode
            nextNode = currNode.next
        if mapping[head.val] > 1:
            return head.next
        return head
        
        