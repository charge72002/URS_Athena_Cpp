#include <iostream>
#include <string>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
int calculateMonths(double bal, double monthly)
{
	int months{0};
	while(bal > 0)
	{
		bal-= monthly;
		months++;
	}
	return months;
}
int main(int argc, char** argv) {
	double balance, monthlyPmt;
	
	cout<<"Enter initial loan balance: ";
	cin>>balance;
	cout<<"Enter monthly payment: ";
	cin>>monthlyPmt;
	
	cout<<"Your loan will be paid off in "<<calculateMonths(balance, monthlyPmt)<<" months"<<endl;

	return 0;
}
