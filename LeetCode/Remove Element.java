// Title: Remove Element
// Runtime: 0 ms
// Memory: 36.2 MB

// Time Complexity: O(n)
// Space Complexity: O(1)
class Solution {
    public int removeElement(int[] nums, int val) {
        int i = 0;
        for (; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[0] = nums[i];
                break;
            } 
        }
        if (i >= nums.length) {
            return 0;
        }
        int ctr = 1;
        for (int j = i + 1; j < nums.length; j++) {
            if (nums[j] != val) {
                nums[ctr++] = nums[j];
            }
        }
        return ctr;
    }
}