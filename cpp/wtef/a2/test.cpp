#include <iostream>
#include <stack>

using namespace std;

int main(){
	stack <char> stk;
	stk.push('(');
	stk.push('(');
	while (!stk.empty()){
		cout << stk.top() << endl;
		stk.pop();
	}
	return 0;
}
