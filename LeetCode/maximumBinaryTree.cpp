//Definition for a bianry tree node
struct TreeNode {
   int val;
   TreeNode *left;
   TreeNode *right;
   TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
  
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

void trimLeftTrailingSpaces(string &input) {
    input.erase(input.begin(), find_if(input.begin(), input.end(), [](int ch) {
        return !isspace(ch);
    }));
}

void trimRightTrailingSpaces(string &input) {
    input.erase(find_if(input.rbegin(), input.rend(), [](int ch) {
        return !isspace(ch);
    }).base(), input.end());
}

vector<int> stringToIntegerVector(string input) {
    vector<int> output;
    trimLeftTrailingSpaces(input);
    trimRightTrailingSpaces(input);
    input = input.substr(1, input.length() - 2);
    stringstream ss;
    ss.str(input);
    string item;
    char delim = ',';
    while (getline(ss, item, delim)) {
        output.push_back(stoi(item));
    }
    return output;
}

string treeNodeToString(TreeNode* root) {
    if (root == nullptr) {
      return "[]";
    }

    string output = "";
    queue<TreeNode*> q;
    q.push(root);
    while(!q.empty()) {
        TreeNode* node = q.front();
        q.pop();

        if (node == nullptr) {
          output += "null, ";
          continue;
        }

        output += to_string(node->val) + ", ";
        q.push(node->left);
        q.push(node->right);
    }
    return "[" + output.substr(0, output.length() - 2) + "]";
}

int main() {
    string line;
    while (getline(cin, line)) {
        vector<int> nums = stringToIntegerVector(line);
        
        TreeNode* ret = Solution().constructMaximumBinaryTree(nums);

        string out = treeNodeToString(ret);
        cout << out << endl;
    }
    return 0;
}
