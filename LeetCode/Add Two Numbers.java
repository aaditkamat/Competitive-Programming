// Title: Add Two Numbers
// Runtime: 20 ms
// Memory: 29.6 MB

class Solution {
    int carry = 0;
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if (l1 == null && l2 == null){
            if (carry == 1) {
                return new ListNode(1);
            }
            return null;
        }
        if (l1 == null) {
            int result = l2.val + carry;
            ListNode current = new ListNode(result % 10);
            carry = result / 10;
            current.next = addTwoNumbers(null, l2.next); 
            return current;
        }
        if (l2 == null) {
            int result = l1.val + carry;
            ListNode current = new ListNode(result % 10);
            carry = result / 10;
            current.next = addTwoNumbers(l1.next, null); 
            return current;
        }
        int result = l1.val + l2.val + carry;
        ListNode current = new ListNode(result % 10);
        carry = result / 10;
        current.next = addTwoNumbers(l1.next, l2.next); 
        return current;
    }
}

