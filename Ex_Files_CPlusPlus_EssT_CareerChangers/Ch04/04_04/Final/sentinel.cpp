#include <iostream>
#include <string>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	string input;
	cout<<"Enter the name of the first student: ";
	cin>>input;
	while(input != "q")
	{
		cout<<"You entered "<<input<<". Enter the next name (q to quit): ";
		cin>>input;
	}
	return 0;
}
