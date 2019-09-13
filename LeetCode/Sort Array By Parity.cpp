// Title: Sort Array By Parity
// Runtime: 40 ms
// Memory: 2.3 MB

class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        vector<int> B;
        for (vector<int>::iterator it = A.begin(); it != A.end(); ++it) {
            if (*it % 2 == 0) 
                B.emplace(B.begin(), *it);
            else
                B.emplace_back(*it);
        }
        return B;
    }
};