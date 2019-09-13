// Title: Stone Game
// Runtime: 4 ms
// Memory: 1 MB

class Solution {
public:
    bool stoneGame(vector<int>& piles) {
        int first = 0, second = 0;
        for (int i = 0; i < piles.size(); i++) {
            if (i % 2 == 0) {
                first += piles[i];
            } else {
                second += piles[i];
            }
        }
        return first != second;
    }
};