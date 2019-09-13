// Title: Reverse String
// Runtime: 8 ms
// Memory: 1.5 MB

class Solution {
public:
    string reverseString(string s) {
        string new_s;
        for (string::reverse_iterator it = s.rbegin(); it != s.rend(); ++it) {
            new_s.push_back(*it);
        }
        return new_s;
    }
};