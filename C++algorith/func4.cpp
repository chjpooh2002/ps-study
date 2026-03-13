#include <iostream>
using namespace std;

int main() {
	int n;
	cin >> n;
	int max = 0;
	for (int i = 1;  i <= n; i *= 2) {
		if (i > max) max = i;
	}
	cout << max;
}