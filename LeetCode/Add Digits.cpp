// Title: Add Digits
// Runtime: 4 ms
// Memory: 827.4 KB

class Solution {
public:
    int addDigits(int num) {
        while (num >= 10) {
            int cp = num;
            int sum = 0;
            while (cp > 0) {
                sum += cp % 10;
                cp /= 10;
            }
            num = sum;
        }
        return num;
    }
};