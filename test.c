#include <iostream>
using namespace std;

void f(int& a, int& b){
	a = 1;
	b = 1;
}

int main(){
	float a = 6.6;
	int b = 23;
	f(a, b);
	cout << a << " " << b << endl;
}
