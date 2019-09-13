# Title: Merge Two Sorted Lists
# Runtime: 44 ms
# Memory: 14 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def removeDummy(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        curr = head
        while curr and curr.next and curr.next.next:
            curr = curr.next
        curr.next = None
        return head
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = ListNode(0) #add dummy node
        head = curr
        while l1 or l2:
            if (l1 and l2 and l1.val < l2.val) or (l1 and not l2):
                curr.val = l1.val
                l1 = l1.next
            else:
                curr.val = l2.val
                l2 = l2.next
            curr.next = ListNode(0)
            curr = curr.next
        return self.removeDummy(head)
        