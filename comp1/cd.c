#include<stdio.h>

int min(int c, int d)
{
	if(c <= d*2)
		return d;
	return c-d;
}

int check(int c, int d, int l)
{
	int m = min(c, d);
	return (m*4 <= l) && (l <= (c+d)*4);
}

int main()
{
	int test;
	scanf("%d", &test);
	int c, d, l, i, t;
	int out[test];
	for (t=0; t<test; t++)
	{
		scanf("%d %d %d",	&c, &d, &l);
		out[t] = check(c, d, l);
	}
	for (i=0; i<test; i++)
		printf(out[i] ? "yes\n" : "no\n");
	return 0;
}
