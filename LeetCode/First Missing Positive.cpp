// Title: First Missing Positive
// Runtime: 4 ms
// Memory: 1.5 MB

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        if (nums.size() == 0) {
            return 1;
        }
        int max = *max_element(nums.begin(), nums.end());
        for (int i = 1; i <= max + 1; i++) {
            if (find(nums.begin(), nums.end(), i) == nums.end()) {
                return i;
            }
        }
        return 0;
    }
};