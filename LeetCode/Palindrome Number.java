// Title: Palindrome Number
// Runtime: 81 ms
// Memory: 27.1 MB

class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0)
            return false;
        int length = 0, num = x;
        while (num != 0) {
            num /= 10;
            length++;
        }
        int[] digits = new int[length];
        num = x;
        for (int i = 0; i < length; i++){
            digits[i] = num % 10;
            num /= 10;
        }
        for (int i = 0, j = length - 1; i != j && j >= 0; i++, j--) {
            if (digits[i] != digits[j]) {
                return false;
            }
        }
        return true;
    }
}