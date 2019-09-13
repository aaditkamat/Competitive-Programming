// Title: Happy Number
// Runtime: 4 ms
// Memory: 827.4 KB

class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> history;
        int num = n;      
        while (num != 1 && history.find(num) == history.end()){
            history.insert(num);
            int cp = num, sum = 0;
            while (cp > 0) {
                sum += (cp % 10) * (cp % 10);
                cp /= 10;
            }
            num = sum;
        }
        return num == 1;    
    }
};