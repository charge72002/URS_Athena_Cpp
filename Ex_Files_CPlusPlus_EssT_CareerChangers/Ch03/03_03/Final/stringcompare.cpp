#include <iostream>
#include <string>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	string s1, s2, s3;
	cout<<"Enter three words: ";
	cin>>s1;
	cin>>s2;
	cin>>s3;
	if(s1.compare(s2)<0)
	{
		if(s2.compare(s3)<0)
		{
			cout<<s1<<", "<<s2<<", "<<s3<<endl;
		}
		cout<<s1<<", "<<s3<<", "<<s2<<endl;
	}
	else if(s2.compare(s3)<0)
		{
			if(s1.compare(s3)<0)
			{
				cout<<s2<<", "<<s1<<", "<<s3<<endl;
			}
			cout<<s2<<", "<<s3<<", "<<s1<<endl;
		}
		else
			cout<<s3<<", "<<s2<<", "<<s1<<endl;
	return 0;
}
