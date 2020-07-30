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
	int test, t, i;
	scanf("%d", &test)
	return 0;
}
