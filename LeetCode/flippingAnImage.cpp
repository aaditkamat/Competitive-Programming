class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
        for_each(begin(A), end(A), [](vector<int> &image) {
           reverse(begin(image), end(image));
           for_each(begin(image), end(image), [](int &bit) {
               bit = 1 - bit;
           });
        });
        return A;
    }
};



