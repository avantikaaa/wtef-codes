#include <iostream>
#include <stack>

using namespace std;

long int strToInt(string str){
    long int num = 0;
    for (int i=0; i<str.length(); i++){
        num *= 10;
        num += int(str[i]) - int('0');
    }
    return num;
}

long int decodeString(string arr){
    string num;
    stack <int> stk;
    int len = arr.length();
    
    for (int i=0; i<=len; i++){
        stk.push(i+1);
        if(i == len || arr[i] == 'I'){
            while (!stk.empty()){
                num += to_string(stk.top());
                stk.pop();
            }
        }
    }
    
    return strToInt(num);
}

int main(){
    string arr;
    cin >> arr;
    cout << decodeString(arr) << endl;
    return 0;
}
