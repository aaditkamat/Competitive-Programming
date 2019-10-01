# Title: Remove Duplicates from Sorted List
# Runtime: 48 ms
# Memory: 13.8 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        prev, curr = head, head.next
        while curr:
            if prev.val == curr.val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return head
                
            
        