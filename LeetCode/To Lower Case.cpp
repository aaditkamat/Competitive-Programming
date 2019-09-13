// Title: To Lower Case
// Runtime: 0 ms
// Memory: 860.2 KB

class Solution {
public:
    string toLowerCase(string str) {
        for_each(begin(str), end(str), [](char& ch) {
            if (ch >= 65 && ch <= 90)
                ch += 32;
        });
        return str;
    }
};