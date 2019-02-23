#include<iostream>
#include<string>
#include<algorithm>
#include<cmath>

using namespace std;

class Solution {
public:
    int reverse(int x) {
        string result = to_string(abs(x));
        string new_string;
        for (int i = result.size() - 1; i >= 0; i--) {
            new_string.push_back(result.at(i));
        }
        try {
         if (x > 0)
          return stoi(new_string);
         else
          return -1 * stoi(new_string);   
        } catch(exception& e) {
            return 0;
        }
    }
};

int main() {
   int first = Solution().reverse(123); 
   cout << first << endl;
   int second = Solution().reverse(-123);
   cout << second << endl;
   int third = Solution().reverse(120);
   cout << third << endl;
   return 0;
}
  
