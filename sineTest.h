#ifndef _SINE_TEST_H_
#define _SINE_TEST_H_
#include <cstdlib>
#include <cmath>

using namespace std;

class SinePrototype
{
    public:
    // Overload the constructor
	SinePrototype()
		{
        // When you overload this constructor, use it to initialize constants
        // and array storage 
        }

    // Overload the function with your function
	virtual double sine(double x) {
        return sin(x);
	}
};
#endif
