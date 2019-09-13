// Title: Maximum Binary Tree
// Runtime: 104 ms
// Memory: 1.4 MB

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> find_max(vector<int>& nums) {
        vector<int> max_details;
        max_details.push_back(nums.at(0));
        max_details.push_back(0);
        for (int i = 1; i < nums.size(); i++) {
            if (nums.at(i) > max_details.at(0)) {
                max_details.insert(max_details.begin(), nums.at(i));
                max_details.insert(max_details.begin() + 1, i) ;
            }
        }
        return max_details;
    }
    
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        if (nums.empty()) {
            return NULL;
        }
        vector<int> max_details = find_max(nums);
        int max = max_details.at(0);
        int pos = max_details.at(1);
        TreeNode* root = new TreeNode(max);
        vector<int> left(begin(nums), begin(nums) + pos);
        vector<int> right(begin(nums) + pos + 1, end(nums));
        root -> left = constructMaximumBinaryTree(left);
        root -> right = constructMaximumBinaryTree(right);
        return root;
    }
};