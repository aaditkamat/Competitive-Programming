#include<iostream>
#include<string>

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

int stringToInteger(string input) {
    return stoi(input);
}

int main() {
    string line;
    while (getline(cin, line)) {
        int num = stringToInteger(line);
        
        int ret = Solution().findComplement(num);

        string out = to_string(ret);
        cout << out << endl;
    }
    return 0;
}
