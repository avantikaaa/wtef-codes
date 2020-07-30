#include <iostream>
#include <vector>

using namespace std;

int isStrong(int n){
    int factorial[] = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880};
    int sum = 0;
    int tmp = n;
    while (tmp > 0){
        sum += factorial[tmp % 10];
        tmp /= 10;
    }
    return sum == n;
}

int main()
{
    int n;
    cin >> n;
    vector <int> strongNumbers;
    for (int i = 1; i < n; i++){
        if (isStrong(i))
            strongNumbers.push_back(i);
    }
    for (auto i = strongNumbers.begin(); i != strongNumbers.end(); i++)
        cout << *i << " ";
    cout << endl;
    return 0;
}
