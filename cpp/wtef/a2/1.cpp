#include <iostream>
#include <stack>

using namespace std;

int redundant(string inp){
    stack <char> stk;
    int i = 0;
    while (i<inp.length()){
        if (inp[i] == ')'){
            if (stk.top() != '('){
            	int flag = 0;
                while (stk.top() != '('){
                	cout << "Pop " << stk.top() << endl;
                	if (stk.top() == '+' || stk.top() == '-' || stk.top() == '*' || stk.top() == '/')
                        flag = 1;
                    stk.pop();
                }
                if (!flag)
                	return 1;
                cout << "Pop " << stk.top() << endl;
                stk.pop();
            }
            else
                return 1;
        }
        else{
        	cout << "Push " << inp[i] << endl;
            stk.push(inp[i]);
        }
        i++;
    }
    while(!stk.empty()){
    	cout << stk.top() << endl;
        if (stk.top() == '(' || stk.top() == ')')
            return 1;
        stk.pop();
    }
    return 0;
}

int main(){
    string inp;
    getline(cin, inp);
    cout << redundant(inp) << endl;
    return 0;
}
