#include <iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

vector <int> getFactors(int n)
{
	vector <int> factors;
	int i = 1;
	while (i*i < n)
	{
		if(n%i == 0)
		{
			factors.push_back(i);
			factors.push_back(n/i);
		}
		i++;
	}
	if(i*i == n)
		factors.push_back(i);
	sort(factors.begin(), factors.end());
	return factors;
}

int kthFactor(int n, int k)
{
	vector <int> factors = getFactors(n);
	return factors.at(k-1);
}

int main()
{
	int n, k;
	cin >> n >>k;
	cout <<kthFactor(n, k) << endl;
	return 0;
}

