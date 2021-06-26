#include <iostream>
#include <vector>
#include <array>
/*This is a directive. It talks to the preprocessor and executes before actual compilation.
  Essentially adds lines of code used in the package
  Common directives include:
  <iostream> stream I/O 
  <iomanip> custom #decimal places (width/precision)
  <fstream> file I/O
  <sstream> streing I/O

  Common Standard Library Templates (STL):
  <string>, <vector>, <array>
  <list> doubly linked, <deque> FIFO, <stack> LIFO
*/

using namespace std;

//Taken directly from video
//if x<y TRUE return x, if FALSE return y
#define MIN(x, y) ((x<y)? x:y)

//#define count(x, y) (for(int i=x; i<=y; x++){cout<<x;cout<<"\n"})

/*Can use main(int argc, char** argv)
  for command line arguments
  argc is # of arguments, argv is argument vector with argc values
*/
int main() {
  string message = "Hello World\n";
  cout << message;
  //returns 0 by default b/c this is the main method
#define C 300000; //use #define for variables and methods
  cout << C ;
  cout << "\n";
  cout << MIN(2, 3);
  cout << "\n";
  //"initializer list for C++11, will give additional warnings as necessary"
  float x {999.10};
  cout << x;
  cout << "\n";
  //Will auto-assign variable type
  auto y {"999"};
  cout << y;
  cout << "\n";

  vector<char> letter_vector{'a', 'b', 'c'};
  for(char i : letter_vector){cout<<i;}
  cout << "\n";
  
  array<char, 5> letter_array{'a', 'b', 'c', 'd', 'e'};
  for(char i : letter_array){cout<<i;}
  cout << "\n\n";
  
  for(int i {0}; i<10; i++){
    cout << i;
    cout << "\n";
  }
  //count(0, 5);
}
