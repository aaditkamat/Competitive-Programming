class Solution {
public:
    bool isPalindrome(int x) {
       if (x < 0)
            return false;
        int length = 0, num = x;
        while (num != 0) {
            num /= 10;
            length++;
        }
        if (length == 0)
            return true;
        int digits[length];
        num = x;
        for (int i = 0; i < length; i++){
            digits[i] = num % 10;
            num /= 10;
        }
        for (int i = 0, j = length - 1; i != j && j >= 0; i++, j--) {
            if (digits[i] != digits[j]) {
                return false;
            }
        }
        return true;
    } 
};

int stringToInteger(string input) {
    return stoi(input);
}

string boolToString(bool input) {
    return input ? "True" : "False";
}

int main() {
    string line;
    while (getline(cin, line)) {
        int x = stringToInteger(line);
        
        bool ret = Solution().isPalindrome(x);

        string out = boolToString(ret);
        cout << out << endl;
    }
    return 0;
}
