#include <iostream>
#include <cstlib>

using namespace std;

void getString(int length, char reqStr[], int* maxScore, char *closest){
    srand(time(0));
    char str[length];
    int score = 0;
    for (int i = 0; i < length; i++){
        str[i] = rand()%length;
