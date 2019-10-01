// Title: Remove Duplicates from Sorted Array
// Runtime: 1 ms
// Memory: 39.6 MB

// Time Complexity: O(n)
// Space Complexity: O(1)
class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        int ctr = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[ctr]) {
                nums[++ctr] = nums[i];
            }
        }
        return ctr + 1;
    }
}