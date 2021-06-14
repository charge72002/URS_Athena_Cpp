#include <iostream>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	int totalGoals=0;
	int goals, game = 1, numGames=0;
	cout<<"How many games did you play this season?";
	cin>>numGames;
//	while(goals>=0)
	for(int i = 0; i<numGames;i++)
	{
		cout<<"Enter goals for game "<<game<<":";
		cin>>goals;
		if(goals < 0)
			break;
		totalGoals += goals;
		game++;
	}
	cout<<"The total goals for your team this season was: "<<totalGoals<<endl;
	return 0;
}
