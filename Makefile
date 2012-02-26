# Makefile for interpolation template
#
# Add your headerfile to the sineTest: line.

sineTest: sineTest.h sineTest.cpp ChebSine.h LinearSine.h
	g++ -o sineTest sineTest.cpp

all: sineTest

clear:
	rm -f sineTest
