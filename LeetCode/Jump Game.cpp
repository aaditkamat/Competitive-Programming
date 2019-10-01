// Title: Jump Game
// Runtime: 820 ms
// Memory: 9.9 MB

// Time Complexity: O(nm) where n is the size of array and m is the value in the array
// Sapce Complexity: O(n)
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int table[nums.size()];
        int end = nums.size() - 1;
        for (int i = 0; i < nums.size(); i++) {
            if (i == end) {
                table[i] = 1;
            } else {
                table[i] = -1;   
            }
        }
        for (int start = end - 1; start >= 0; start--) {
            bool flag = true;
            for (int i = 1; i <= nums[start]; i++) {
                if (start + i >= end || table[start + i] == 1) {
                    table[start] = 1;
                    flag = false;
                }
            }
            if (flag) {
             table[start] = 0;   
            }
        }
        if (table[0] == 1) {
            return true;
        }
        return false;
    }
};