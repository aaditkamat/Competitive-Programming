// Title: Integer to Roman
// Runtime: 56 ms
// Memory: 17.2 MB

class Pair {
    public:
    string letter;
    int value;
    Pair(string letter, int val) {
        this -> letter = letter;
        this -> value = val;
    }
};

class Solution {
public:
    vector<Pair> symbol_map {Pair("M", 1000), Pair ("CM", 900), Pair("D", 500), Pair("CD", 400), Pair("C", 100), Pair("XC", 90), Pair("L", 50), Pair("XL", 40), Pair("X", 10), Pair("IX", 9), Pair("V", 5), Pair("IV", 4), Pair("I", 1)};
    string intToRoman(int num) {
      string x("");
      for (const auto& item: symbol_map) {
         if (item.value == num) {
             return item.letter;
         }
         if (num > item.value) {
             x.append(item.letter);
             return x.append(intToRoman(num - item.value));
         }
      }
    }
};