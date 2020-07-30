#include <iostream>
#include <random>
#include <fstream>
#include <cstring>

using namespace std;

const string ALPHABETS("abcdefghijklmnopqrstuvwxyz");
default_random_engine rand_engine;
uniform_int_distribution<size_t> dist(0, ALPHABETS.length() - 1);

string make_word(int how_long) {
    string word;
    for (int i = 0; i < how_long; ++i) {
        word += ALPHABETS[dist(rand_engine)];
    }            
    return word;
}

int isWord (string allWords[], string word){
	return 1;/*
	int left = 0;
	int right = 535500;
	int mid;
	int compare;
	while (left <= right){
		mid = (left + right)/2;
		compare = strcmp(word, allWords[mid]);
		if (compare == 0)
			return 1;
		if (compare > 0)
			left = mid+1;
		else
			right = mid-1;
	}
	return 0;*/
}

int main(int argc, char* argv[]) {

	int letters = stoi(argv[1]);
	int noOfWords = stoi(argv[2]);
	string allWords[535501];
	unsigned int counter = 0;
	
	ifstream dict;
	dict.open("words.txt");
	unsigned int i = 0;
	string word;
	while (getline(dict, word)){
		allWords[i] = word;
		i++;
	}
	
    while(noOfWords > 0) {
    	counter++;
        string word = 
        cout << make_word(letters) << endl;
        return 0;
        if (isWord(allWords, word)) {
        	cout << counter << " " << word << endl;
        	noOfWords--;
        	counter = 0;
        }

    }
    cout << endl;
    return 0;
}

