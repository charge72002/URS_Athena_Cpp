#include <iostream>
#include <iomanip>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	string lName;
	const double commission{.06};
	const double listingAgent{.015};
	double salesprice, sellerCost, agentsCommission;
	cout<<"Enter homeowners last name: ";
	cin>>lName;
	cout<<"Enter the sales price for the house: (no commas or decimal points)";
	cin>>salesprice;
	sellerCost = commission*salesprice;
	agentsCommission = listingAgent*salesprice;
	cout<<"\tHome Owner\tPrice of Home\tSeller's Cost\tAgent's Commission\n";
	cout<<"\t"<<left<<setw(16)<<lName<<"$"<<salesprice<<"\t\t$"<<sellerCost<<"\t\t$"<<agentsCommission<<endl;
	return 0;
}
