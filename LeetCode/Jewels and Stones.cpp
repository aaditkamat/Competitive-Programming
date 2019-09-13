// Title: Jewels and Stones
// Runtime: 4 ms
// Memory: 1.9 MB

class Solution {
public:
    int numJewelsInStones(string J, string S) {
        int total = 0;
        for (char c: J) {
            total += count(begin(S), end(S), c);
        }
        return total;
    }
};