#include<bits/stdc++.h>

using namespace std;

int min_pieces(int n, int i, int a, int b) {
	if (i <= a)
		return min(floor(a / i), floor(b / (n - i)));
	else
		return min(floor(a / (n - i)), floor(b / i));
}

int maximized_min_pieces(int n, int a, int b) {
	vector<int> result;
	for (int i = 1; i < n; i++) {
			result.push_back(min_pieces(n, i, a, b));
	}
	return *max_element(result.begin(), result.end());
}

int main() {
	int n, a, b;
	cin >> n;
	cin >> a;
	cin >> b;
	cout << maximized_min_pieces(n, a, b) << endl;
}