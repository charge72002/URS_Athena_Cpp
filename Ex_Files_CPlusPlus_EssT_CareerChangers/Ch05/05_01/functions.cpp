#include <iostream>
#include <string>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
double balance, monthlyPmt;
	int months{0};
	cout<<"Enter initial loan balance: ";
	cin>>balance;
	cout<<"Enter monthly payment: ";
	cin>>monthlyPmt;
	while(balance > 0)
	{
		balance -= monthlyPmt;
		months++;
	}
	cout<<"Your loan will be paid off in "<<months<<" months"<<endl;

	return 0;
}
