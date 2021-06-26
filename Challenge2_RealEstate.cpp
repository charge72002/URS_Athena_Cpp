#include<iostream>
using namespace std;
#include<string>
#include<iomanip>

int main() {
  //Format output
  //cout<<left;
  
  //Ask user for homeowner name
  cout<<"Enter the homeowner's last name: ";
  string name;
  cin>>name; //stops at first whitespace
  //getline(cin, name); //stops at endline aka enter
  
  //Ask user for current listing price
  cout<<"Enter the sales price for the house: (no commas or decimal points) ";
  int price;
  cin>>price;
  
  //Print last name/selling price/
  //seller's cost(6%)/comission(1.5%)

  //cout<<"\tHome Owner\tPrice of Home\tSeller's Cost\tAgent\'s Comission"<<endl;
  //cout<<"\t"<<name<<"\t\t$"<<price<<"\t$"<<(price*0.06)<<"\t$"<<(price*0.015)<<endl;
  
  //cout<<left<<setw(18)<<"\tHome Owner"<<setw(18)<<"Price of Home"<<setw(18)<<"Seller's Cost"<<setw(18)<<"Agent\'s Comission"<<endl;
  //cout<<"\t"<<setw(18)<<name<<"$"<<price<<setw(18)<<"$"<<(price*0.06)<<setw(18)<<"$"<<(price*0.015)<<endl;

  cout<<"\tHome Owner\tPrice of Home\tSeller's Cost\tAgent\'s Comission"<<endl;
  cout<<left<<"\t"<<setw(12)<<name<<"\t$"<<price<<"\t\t$"<<(price*0.06)<<"\t\t$"<<(price*0.015)<<endl;

}
