#include <iostream>

using namespace std;

int decodeString(string arr){
	int number = 0;
	int currMax = 0;
	int last = 0;
	int j;
	int nextD;
	int len = arr.length();
	
	for (int i = 0; i < len; i++){
		nextD = 0;
		if (arr[i] == 'I'){
			j = i+1;
			while (arr[j] == 'D' && j < len){
				nextD++;
				j++;
			}
			
			if (i == 0){
				currMax = nextD + 2;
				number *= 10;
				number += ++last;
				number *= 10;
				number += currMax;
				
				last = currMax;
			}
			else{
				currMax += nextD + 1;
				last = currMax;
				
				number *= 10;
				number += last;
			}
			for (int k = 0; k < nextD; k++){
				number *= 10;
				number += --last;
				i++;
			}
		}
		
		else if (arr[i] == 'D'){
			if (i == 0){
				j = i+1;
				while (arr[j] == 'D' && j < len){
					nextD++;
					j++;
				}
				
				currMax = nextD + 2;
				
				number *= 10;
				number += currMax;
				number *= 10;
				number += currMax - 1;
				
				last = currMax - 1;
			}
			
			else{
				number *= 10;
				number += --last;
			}
		}
	}
		
	return number;
}

int main(){
	string arr;
	cin >> arr;
	cout << decodeString(arr) << endl;
	return 0;
}
