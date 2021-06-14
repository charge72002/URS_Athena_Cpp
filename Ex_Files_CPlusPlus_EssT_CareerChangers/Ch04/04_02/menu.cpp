#include <iostream>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	//create a menu of lunch choices
	int choice;
	cout<<"\tChoose one: \n";
	cout<<"\t\t1. Hot Dog\t\t$1.95\n";
	cout<<"\t\t2. Chili Dog\t\t$2.50\n";
	cout<<"\t\t3. Hamburger\t\t$2.95\n";
	cout<<"\t\t4. Cheeseburger\t\t$3.50\n";
	cout<<"\t\t5. Water\t\t$1.50\n";
	cin>>choice;
	switch(choice)
	{
		case 1:
			cout<<"You chose a Hot Dog.";
			break;
		case 2:
			cout<<"You chose a Chili Dog."; break;
		case 3:
			cout<<"You chose a hamburger."; break;
		case 4: 
			cout<<"You chose a cheeseburger."; break;
		case 5: 
			cout<<"You chose water."; break;
		default:
		cout<<"Invalid choice."; break;	
				
	}
	return 0;
}
