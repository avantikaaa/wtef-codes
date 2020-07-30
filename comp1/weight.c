#include<stdio.h>

void merge(int a[], int left, int middle, int right)	//To split and merge an array
{
	int i, j, k;
	i = 0;
	j = 0;
	int n1 = middle-left+1;
	int n2 = right - middle;
	int m[n1];
	int n[n2];
	for (int t = 0; t<n1; t++)
		{m[t] = a[left+t];}

	for (int t=0; t<n2; t++)
		{n[t] = a[middle+1+t];}

	k = left;
	while(i<n1 && j<n2)					//Comparing the elements of 2 sorted arrays
	{
		if (m[i]<=n[j])
		{
			a[k] = m[i];
			i++;
		}
		else
		{
			a[k] = n[j];
			j++;
		}
		k++;
	}
	while (i<n1)						//If j goes out of bounds
	{
		a[k] = m[i];
		i++;
		k++;
	}
	while (j<n2)						//If i goes out of bounds
	{
		a[k] = n[j];
		j++;
		k++;
	}
						
}

void MergeSort(int a[], int left, int right)		//Reccursive function
{
	if (right-left>0)
	{
		int middle =(right+left)/2;
		MergeSort(a, left, middle);
		MergeSort(a, middle+1, right);
		merge(a, left, middle, right);
		
	}
}	

int main()
{
	int test;
	scanf("%d", &test);
	int n, k, s1, s2, i;
	for(int t=0; t<test; t++)
	{
		scanf("%d %d", &n, &k);
		int arr[n];
		for (i=0; i<n; i++)
			scanf("%d", &arr[i]);
		MergeSort(arr, 0, n-1);
		s1 = 0;
		s2 = 0;
		for(i=0; i<k; i++)
			s1 += arr[i];
		for (i=k; i<n; i++)
			s2 += arr[i];
		printf("%d\n", s2-s1);
	}
	return 0;
}


