#include <iostream>
#include <string>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	int a = 5, b = 7, c = 11;
	double average = (a + b + c)/3.0;
	cout<<average<<endl;
	a += 3;
	cout<<"a: "<<a<<endl;
	int r;
	r = c % 2;
	cout<<"remainder: "<<r<<endl;
	return 0;
}
