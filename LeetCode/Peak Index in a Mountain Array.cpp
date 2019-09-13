// Title: Peak Index in a Mountain Array
// Runtime: 16 ms
// Memory: 9.7 MB

class Solution {
public:
    int peakIndexInMountainArray(vector<int>& A) {
        return find(A.begin(), A.end(), *max_element(A.begin(), A.end())) - A.begin();
    }
};