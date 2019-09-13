// Title: Unique Binary Search Trees
// Runtime: 0 ms
// Memory: 831.5 KB

class Solution {
public:
    int countTrees(int n, int values[]) {
        if (values[n - 1] != 0) {
            return values[n - 1];
        }
        int result = 2 * countTrees(n - 1, values);
        for (int i = 2; i < n; i++) {
            result += countTrees(i - 1, values) * countTrees(n - i, values);
        }
        values[n - 1] = result;
        return result;
    }
    int numTrees(int n) {
        int values[n];
        values[0] = 1;
        for (int i = 1; i < n; i++) {
            values[i] = 0;
        }
        return countTrees(n, values);
    }
};