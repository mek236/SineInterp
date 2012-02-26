#ifndef _CHEB_SINE_H_
#define _CHEB_SINE_H_
#include <cmath>
#include <vector>
#include "sineTest.h"
#include <iostream>
#include <cstdio>
#include <fstream>

#define ORDER 10
// In c++, structs are much like classes, except they default to public
// class LinearSine : public SinePrototype would also work here
struct ChebSine : SinePrototype
{
	private:
		vector<double> xx;
		vector<double> sineX;
		int Npoints;
		int Nintervals;
		double co[ORDER];

	public:
	// Define your functions here 
	// Class Constructor
	ChebSine(const int nn) : SinePrototype()  
	{
		// Initialize and prepare interpolation of sine
		Nintervals = nn;
		Npoints = nn + 1;
		xx.resize(Npoints);
		sineX.resize(Npoints);

		// Get coefficients from file
      ifstream inFile("chebcoeff.txt");
      int n = 0;
		double coeffI;
		while (inFile >> coeffI && n < ORDER) {
			co[n++] = coeffI;
			//cout << co[n-1]<<"\n";
		}
		inFile.close();

		for(int i = 0; i < Npoints; i++) {
			xx[i] = i*2.*M_PI/Nintervals;
			sineX[i] = sin(xx[i]); 
		}
	}

	// Your sine function
	double sine(double x) {
		int j = (int)(x / (2. * M_PI) * Nintervals);
		// This could probably be faster if we remove the if statement
		if (j>=Nintervals) j = Nintervals-1;
			return sineX[j] + ((x-xx[j])/(xx[j+1]-xx[j]))*(sineX[j+1]-sineX[j]);
		}
	};
#endif
