#include <iostream>
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
  cout << "Hello World!!\n";
  //returns 0 by default b/c this is the main method
#define C 300000; //use #define for variables and methods
  cout << C ;
  cout << "\n";
  cout << MIN(2, 3);
  cout << "\n";
  //count(0, 5);
}


