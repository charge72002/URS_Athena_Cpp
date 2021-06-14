#include <iostream>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
void getRainfall(double r[12])
{
	for(int i = 0;i<12 ;i++)
	{
		cout<<"Enter rainfall for month: "<<i+1;
		cin>>r[i];
	}
}
int main(int argc, char** argv) {
	double rain[12];
	getRainfall(rain);
	cout<<"Jan\tFeb\tMar\tApr\tMay\tJun\tJul\tAug\tSep\tOct\tNov\tDec\n";
	for(double r:rain)
	{
		cout<<r<<"\t";
	}
	
	return 0;
}
