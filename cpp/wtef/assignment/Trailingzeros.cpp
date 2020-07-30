#include <iostream>

using namespace std;

int trailingZeroes(int n)
{
	int out = 0;
	while (n>5)
	{
		out += n/5;
		n /= 5;
	}
	return out;
}

int main()
{
	int n;
	cin >> n;
	cout << trailingZeroes(n) << endl;
	return 0;
}
