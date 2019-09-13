// Title: Number Complement
// Runtime: 0 ms
// Memory: 1.4 MB

class Solution {
public:
    int findComplement(int num) {
        double length = 0;
        int copy = num;
        while (copy != 0) {
            copy /= 2;
            length++;
        }
        double total = pow(2.0, length) - 1;
        return (int)(total - num);
    }
};
