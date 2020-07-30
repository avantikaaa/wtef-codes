#include <iostream>
#include <cstdlib>

using namespace std;

int possibleTriangles(int i, int j, int a, int b)
{
	return min(i+j, b) - j;
}

int triangles(int a, int b)
{
	int i, j, out = 0;
	for (i = a+1; i < b; i++)
	{
		for (j = i; j < b; j++)
		{
			out += possibleTriangles(i, j, a, b);
		}
	}
	return out;
}

int main()
{
	int a, b;
	cin >> a >> b;
	cout << triangles(a, b) << endl;
	return 0;
}
