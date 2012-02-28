#include "sineTest.h"
#include "LinearSine.h"
#include "ChebSine.h"

#include <cmath>
#include <ctime>
#include <iostream>
#include <limits>
#include <sstream> // Needed for input argument handling
#include <string> // Needed for input argument handling

using namespace std;

void EvaluateYourSine(SinePrototype *yoursine, const char *name);
#define NTIME 10000000
#define NERR 1000000
// tunable parameters
static double randarr[NTIME];

int main(int ARGC, char* ARGV[])
{
	clock_t st, ed;

	// generate an array of random numbers to test the time
	for(int i=0; i<NTIME; i++) {
		randarr[i] = rand()*2.*M_PI/RAND_MAX;
	}

  	int chebOrder;
  	int linOrder;
    if (ARGC > 2) {
        // Check for valid input
        cout << "\nOnly one input: sineTest n\n\n";
        // Note that ARGV[0] is the file name
        // ARGV[1] is the first user input
        return 0;
    } else if (ARGC < 2) {
			cout << "\nYou can input a number after the program name to specify";
			cout << " the order for the\n";
			cout << " interpolation. For instance, 'sineTest 9' will use Chebyshev";
			cout << " polynomials up to\n";
			cout << " and including T_9.\n";
			cout << "Defaulting to order 15...\n\n";
			chebOrder = 15;
			linOrder = chebOrder;
    } else { // Two inputs - file name for ARGV[0], plus user input
			string inp;
			inp = string (ARGV[1]);
			istringstream iss (inp);
			cout << "\nARGV[1] = " << inp << "\n"; // For debugging
			iss >> chebOrder;
			linOrder = chebOrder;
    	if (chebOrder <= 0) { // Check for valid numeric input
    	    cout << "Invalid input; setting to default order (15)\n\n";
    	    chebOrder = 15;
    	    linOrder = 15;
    	    // Note that improvement in Chebyshev accuracy is negligible above
    	    //  about order 21
    	} else if (chebOrder > 1000000) {
    	    cout << "Input above useful maximum for linear; resetting that";
    	    cout << " to order 1,000,000\n";
    	    linOrder = 1000000;
    	    // Need order of about one million to get double precision
    	    cout << "Input above useful maximum for Chebyshev; resetting that";
    	    cout << " to order 15\n\n";
    	    chebOrder = 15;
    	} else if (chebOrder > 35) {
    	    cout << "Input above useful maximum for Chebyshev; resetting that";
    	    cout << " to order 15\n\n";
    	    chebOrder = 15;
    	}
    }

	//int interpOrder=15; // Old version
    // For debugging:
    cout << "Chebyshev interpolation order:  " << chebOrder << "\n";
    cout << "Linear interpolation divisions: " << linOrder << "\n\n";
	// Instantiate machineSine, linearSine
	// Add your sine class and call EvaluateYourSine with your class instance.
	SinePrototype machineSine;
	LinearSine linear(linOrder);
	ChebSine chebsin(chebOrder);
    
	EvaluateYourSine(&machineSine, "machine sine");
	EvaluateYourSine(&chebsin, "Chebyshev sine");
	// chebsin uses Clenshaw's recurrence; see Numerical Recipes p. 237
	EvaluateYourSine(&linear, "linear sine");
}

void EvaluateYourSine(SinePrototype *yoursine, const char *name) {
    clock_t st, ed;
    double tmp;
    st = clock();
    for(int i=0; i<NTIME; i++) {
    // We add up the results to keep the optimizing compiler from removing the line
        tmp += yoursine->sine(randarr[i]);
    }
    ed = clock();
    cout << "Time for " << name << ":" << endl;
    cout << (double(ed)-double(st))/CLOCKS_PER_SEC << "s per " << NTIME << " repetitions" << endl;

    // Evaluate errors
    double errorMax = 0.;
    double err;
    for(double t=0.; t<2.*M_PI; t += 2.*M_PI/NERR) {
       err = abs(yoursine->sine(t) - sin(t));
       if (errorMax <= err) errorMax = err; 
    }

    // print error
    cout << "Maximum Error = " << errorMax << endl << endl;
}
