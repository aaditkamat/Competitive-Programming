# Title: Swap Nodes in Pairs
# Runtime: 32 ms
# Memory: 13.7 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        curr_node, prev_node = head, None
        while curr_node and curr_node.next:
            next_node = curr_node.next
            if not prev_node:
                head = next_node
            else:
                prev_node.next = next_node
            curr_node.next = next_node.next
            next_node.next = curr_node
            prev_node = curr_node
            curr_node = curr_node.next
        return head