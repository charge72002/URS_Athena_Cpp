#include <iostream>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
double principal{0};
double rate {0};
double time {0};
//prototypes/function signatures for my functions
void getValues();
double getInterest();
	
int main(int argc, char** argv) {
	
	getValues();
	double interest = getInterest();
	cout<<"The amount of interest earned is $"<<interest<<endl;

	
	return 0;
}
void getValues()
{
	cout<<"Enter principal: ";
	cin>>principal;
	cout<<"Enter rate (.99): ";
	cin>>rate;
	cout<<"Duration: ";
	cin>>time;
	
}
double getInterest()
{
	double interest;
	interest = principal*rate*time;
	return interest;
}
