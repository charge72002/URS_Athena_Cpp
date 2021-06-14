#include <iostream>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	double principal{500};
	double rate {.02};
	double time {5};
	double interest;
	interest = principal*rate*time;
	cout<<interest<<endl;
	
	return 0;
}
