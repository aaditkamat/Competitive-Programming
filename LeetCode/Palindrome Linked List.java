// Title: Palindrome Linked List
// Runtime: 3 ms
// Memory: 39.7 MB

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
import java.util.Vector;

// Time Complexity: O(n)
// Space Complexity: O(n)
class Solution {
    Vector<Integer> convertToVector(ListNode head) {
        Vector<Integer> arrayList = new Vector<>();
        while(head != null) {
            arrayList.add(head.val);
            head = head.next;
        }
        return arrayList;
    }
    
    boolean checkPalindromeArrayList(Vector<Integer> arrayList) {
        int start = 0, end = arrayList.size() - 1;
        while (start < end) {
            if ((int)arrayList.get(start) != (int)arrayList.get(end)) {
                return false;
            }
            ++start;
            --end;
        }
        return true;
    }
    
    boolean isPalindrome(ListNode head) {
        Vector<Integer> arrayList = convertToVector(head);
        return checkPalindromeArrayList(arrayList);
    }
}