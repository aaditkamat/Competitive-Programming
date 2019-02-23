#include <algorithm>
#include <string>
#include <iostream>
using namespace std;

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
        return count;
    }
};

int stringToInteger(string input) {
    return stoi(input);
}

int main() {
    string line;
    while (getline(cin, line)) {
        int x = stringToInteger(line);
        getline(cin, line);
        int y = stringToInteger(line);

        int ret = Solution().hammingDistance(x, y);

        string out = to_string(ret);
        cout << out << endl;
    }
    return 0;
}
