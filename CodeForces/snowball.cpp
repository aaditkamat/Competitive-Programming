#include <iostream>

using namespace std;

int main() {
    int w, h, u1, d1, u2, d2;
    cin >> w >> h >> u1 >> d1 >> u2 >> d2;
    int result = w;
    for (int height = h; height >= 0; height--) {
        result += height;
        if (height == d1) {
            result -= u1;
        } else if (height == d2) {
            result -= u2;
        }
        if (result < 0) {
            result = 0;
        }
    }
    cout << result << endl;
    return 0;
}