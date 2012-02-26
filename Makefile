# Makefile for interpolation template
#
# Add your headerfile to the sineTest: line.

sineTest: sineTest.h sineTest.cpp LinearSine.h
	g++ -o sineTest sineTest.cpp

all: sineTest

clear:
	rm -f sineTest
