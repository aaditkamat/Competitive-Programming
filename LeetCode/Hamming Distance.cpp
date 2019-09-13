// Title: Hamming Distance
// Runtime: 4 ms
// Memory: 1.4 MB

class Solution {
public:
    int hammingDistance(int x, int y) {
        if (x == 0 && y == 0) 
            return 0;
        int count = 0;
        while (max(x, y) > 0) {
            if (x % 2 != y % 2) {
                count++;
            }
            x /= 2;
            y /= 2;
        }
        return count;;
    }    
};