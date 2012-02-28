#ifndef _CHEB_SINE_H_
#define _CHEB_SINE_H_
#include <cmath>
#include <vector>
#include "sineTest.h"
#include <iostream>
#include <cstdio>
#include <fstream>

// In c++, structs are much like classes, except they default to public
// class LinearSine : public SinePrototype would also work here   
struct ChebSine : SinePrototype
{
	private:
		int Npoints;
		int Nintervals;
		vector<double> c;
		vector<double> f;
		double A;
		double B;
		double CI;
	public:
	// Define your functions here 
	// Class Constructor
	ChebSine(const int nn) : SinePrototype()  
	{
		// Initialize and prepare interpolation of sine
		double yi;
		bool debug = false;

		Nintervals = nn;
		Npoints = nn + 1;

		c.resize(nn);
		f.resize(nn);

		A=0;
		B=2*M_PI;
		double bma=0.5*(B-A),bpa=0.5*(B+A);
		for(int k=0;k<nn;k++){
			yi=cos(M_PI*(k+0.5)/nn);	// Use zeros of nn-th Chebyshev polynomial as interp nodes
			f[k]=sin(M_PI*(yi)-M_PI);	// Find sin(interpolation nodes)
		}
		for(int j = 0; j < nn ; j++) {
			CI=0.0;
			for( int k=0; k < nn; k++){
				CI+=f[k]*cos(M_PI*j*(k+0.5)/nn);	// Determine coefficients
			}
			c[j]=CI*(2.0/nn);
			if(debug){
				cout << "I=" << j << " C=" << c[j] << "\n";
			}
		}
	}

	double sine(double x) {
		double xi=(x-M_PI)/(M_PI);		//Adjust x to [-1,1]
		double yi=0.0;						//sin(x) estimate
		double d1=0.0,d2=0.0,sv=0.0;
		// Use Clenshaw recursion to find f(x)=sum_n=0^N-1 (c_n*T_n)
		for(int j=Nintervals-1;j>0;j--){
			sv=d1;
			d1=2.0*xi*d1-d2+c[j];
			d2=sv;
		}
		yi=xi*d1-d2+0.5*c[0];			//Final step is different than all others
		return yi;

	}
};
#endif
