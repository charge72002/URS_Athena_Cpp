#include <iostream>
#include <iomanip>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
int calculateArea()
{
	int l, w;
	cout<<"enter the length and width of your room: ";
	cin>>l>>w;
	return l * w;
}
double calculateCost(int area)
{
	if(area < 120)
		return 99;
	double additionalCharge;
	additionalCharge = (area - 120) * .25;
	return 99 + additionalCharge;
}
int main(int argc, char** argv) {
	int roomArea = calculateArea();
	double cost = calculateCost(roomArea);
	cout<<"the total cost to carpet clean your room is: $"<<fixed<<setprecision(2)<<cost<<endl;
	return 0;
}
