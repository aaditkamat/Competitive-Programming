#include<iostream>
#include<cmath>

using namespace std;

int main() {
    int n;
    cin >> n;
    int rows = ceil(sqrt(n));
    cout << rows + ceil(n * 1.0 / rows) << endl;
    return 0;
 }