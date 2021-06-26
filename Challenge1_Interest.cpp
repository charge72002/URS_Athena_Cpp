#include<iostream>
using namespace std;

int main() {
  double principal {500};
  double rate {.02}; //2% annual interest
  double time {5}; //compounded annually over 5 years
  double interest = principal * rate * time;
  cout << interest << endl;
}
