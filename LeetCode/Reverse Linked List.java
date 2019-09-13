// Title: Reverse Linked List
// Runtime: 0 ms
// Memory: 36.9 MB

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode curr_node = null, next_node;
        while(head != null) {
            next_node = new ListNode(head.val);
            next_node.next = curr_node;
            curr_node = next_node;
            head = head.next;
        }
        return curr_node;
    }
}