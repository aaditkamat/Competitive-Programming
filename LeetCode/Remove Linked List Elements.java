// Title: Remove Linked List Elements
// Runtime: 1 ms
// Memory: 39.4 MB

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
// Time Complexity: O(n)
// Space Complexity: O(1)
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        while (head != null && head.val == val) {
            head = head.next;
        }
        if (head == null) {
            return null;
        }
        for (ListNode prev = head, curr = head.next; curr != null; curr = curr.next) {
            if (curr.val == val) {
                prev.next = curr.next;
            }
            else {
                prev = prev.next;
            }
        }
        return head;
    } 
}