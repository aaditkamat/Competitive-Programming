// Title: Minimum Size Subarray Sum
// Runtime: 328 ms
// Memory: 10 MB

class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int size = 1;
        while (size <= nums.size()) {
            int sum = 0;
            for (int i = 0; i < size; i++) {
                sum += nums[i];
            }
            if (sum >= s) {
                return size;
            }
            for (int i = 1; i < nums.size() - size + 1; i++) {
                sum -= nums[i - 1];
                sum += nums[i + size - 1];
                if (sum >= s) {
                    return size;
                }
            }
            size++;
        }
        return 0;
    }
};