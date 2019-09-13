// Title: Flipping an Image
// Runtime: 8 ms
// Memory: 1.2 MB

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