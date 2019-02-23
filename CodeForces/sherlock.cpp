#include<iostream>
#include<cmath>
#include<unordered_map>

using namespace std;

bool is_prime(int n) {
	if (n == 2 || n == 3)
		return true;
	if (n == 4)
		return false;
	for (int i = 2; i <= floor(sqrt(n)); i++) {
		if (n % i == 0)
			return false;
	}
	return true;
}
void color(int n) {
	if (n == 1) {
		cout << 1 << endl;
		cout << 1 << endl;
		return;
	}
	if (n == 2) {
		cout << 1 << endl;
		cout << 1 << " " << 1 << endl;
		return;
	}
	cout << 2 << endl;
	for (int i = 2; i <= n + 1; i++) {
		if (is_prime(i)) {
			cout << 1 << " " ; 
		}
		else {
			cout << 2 << " ";
		}
	}
	cout << endl;
}

int main() {
	int n;
	cin >> n;
	color(n);
	return 0;
}