#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
using namespace std;

int main (int argc, char *argv[])
{
        string LINE;
	ifstream infile;

	if(argc < 2) {
		cout << "Incorrect usage. Please provide the data file name." << endl;
		exit(1);
	}
	
	infile.open (argv[1]);
        while( !infile.eof() ) // Read all the lines from the file.
        {
	        getline(infile, LINE); // store the line in LINE string type
	        cout << LINE; // print the line read form the file before 
			      // going to the next line in the file
        }
	infile.close();       //we are done with the file, hence close the file 
	
	cout << endl;  // add an extra blan line at the end 

	return 0;
}
