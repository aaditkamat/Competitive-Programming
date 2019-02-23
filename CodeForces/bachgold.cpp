#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> max_primes (int num) {
    vector<int> primes;
    if (num <= 1) {
        return primes;
    }
    if (num == 2) {
        primes.push_back(2);
        return primes;
    }
    if (num == 3) {
        primes.push_back(3);
        return primes;
    }
    while (num > 3) {
        primes.push_back(2);
        num -= 2;
    }
    vector<int> current_primes = max_primes(num);
    primes.insert(primes.end(), current_primes.begin(), current_primes.end());
    return primes;
}

void vectorToString(vector<int> primes) {
    for (int i = 0; i < primes.size(); i++) {
        cout << primes.at(i) << " ";
    }
}

int main() {
    int num;
    cin >> num;
    vector<int> primes = max_primes(num);
    cout << primes.size() << endl;
    vectorToString(primes);
    return 0;
}