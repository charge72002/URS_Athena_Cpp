#include <iostream>
using namespace std;
/* this is a sample program 
   to print hello world to the console
*/

int main(int argc, char** argv) {
	//Print out hello world
	cout << "Hello world!\n";
	//#define pi 3.14159
	#ifndef pi
	cout<<"pi was not defined"<<endl;
	#define pi 3.14159
	#endif
	#define MIN(x,y) ((x<y) ? x : y)
	cout<<MIN(5,4);
	bool done = true;
	long longNumber = 123456789L;


	cout<<pi;
	return 0;
}
