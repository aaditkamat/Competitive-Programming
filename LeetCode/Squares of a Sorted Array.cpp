// Title: Squares of a Sorted Array
// Runtime: 136 ms
// Memory: 14.1 MB

class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        for (int& num: A) {
            num *= num;
        }
        sort(A.begin(), A.end());
        return A;
    }
};