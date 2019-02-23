#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size() - 1; i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums.at(i) + nums.at(j) == target) {
                    vector<int> result;
                    result.push_back(i);
                    result.push_back(j);
                    return result;
                }
            }
        }
        return vector<int>();
    }
};

int main() {
    int myints[] = {2, 7, 11, 15};
    int target = 9;
    vector<int> nums(myints, myints + sizeof(myints) / sizeof(int));
    vector<int> result = Solution().twoSum(nums, target);
    for (int i = 0; i < result.size(); i++) {
        cout << result.at(i) << " ";
    }
    cout << endl;
    return 0;
}
