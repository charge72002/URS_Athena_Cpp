#include <iostream>
#include <string>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	string name;
	int year;
	cout<<"Enter the year you were born, and your full name: ";
	cin>>year;
	cin.ignore();
	getline(cin,name);
	//cout<<"Enter your full name: ";
	//cin>>name;
	
	
	cout<<name<<", you will be "<<2017 - year<<" years old this year."<<endl;
	return 0;
}
