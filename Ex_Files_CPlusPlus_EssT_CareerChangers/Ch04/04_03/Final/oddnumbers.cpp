#include <iostream>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	
	for(auto i=1; i<=100; i++)
	{
		if(i%2 != 0)
			cout<<i<<" ";
	}
	
	return 0;
}
