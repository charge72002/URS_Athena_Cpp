#include <iostream>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	double rain[12];
	
	cout<<"Jan\tFeb\tMar\tApr\tMay\tJun\tJul\tAug\tSep\tOct\tNov\tDec\n";
	for(double r:rain)
	{
		cout<<r<<"\t";
	}
	
	return 0;
}
