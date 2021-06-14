#include <iostream>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
double average(double a, double b, double c)
{
	return (a + b + c)/3;
}
double average(double a, double b, double c, double d)
{
	return (a + b + c + d)/4;
}
int main(int argc, char** argv) {
	double w, x, y, z;
	cout<<"Enter three values: ";
	cin>>x>>y>>z;
	double avg;
	avg = average(x,y,z);
	cout<<"Average is: "<<avg<<endl;
	cout<<"Enter another value: ";
	cin>>w;
	avg = average(w, x, y, z);
	cout<<"The new average is: "<<avg;
	
	return 0;
}
