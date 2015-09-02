#README#
Under Linux (and Mac OS), you go into the directory with the four files, and type
    make
which should compile a program "sineTest". Then if you type
    ./sineTest
it should run the program and give you the time taken. (Depending on how
your paths are set, you may not need the initial ./). 

ChebSine.h implements the Clenshaw recursion and Chebyshev interpolation to 
interpolate sin(x) between [0,2pi].

