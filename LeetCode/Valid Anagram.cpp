// Title: Valid Anagram
// Runtime: 12 ms
// Memory: 1.1 MB

class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> sCountOccurences;
        unordered_map<char, int> tCountOccurences;
        if (s.size() != t.size()) {
            return false;
        }
        for (int i = 0; i < s.size(); i++) {
            char currentS = s[i], currentT = t[i];
            if (sCountOccurences.count(currentS) == 0) {
                sCountOccurences[currentS] = 1;
            }
            else {
                sCountOccurences[currentS] += 1;
            }
            if (tCountOccurences.count(currentT) == 0) {
                tCountOccurences[currentT] = 1;
            }
            else {
                tCountOccurences[currentT] += 1;
            }
        }
        return sCountOccurences == tCountOccurences;
    }
};