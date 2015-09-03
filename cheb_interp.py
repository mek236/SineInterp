#!/usr/bin/python
import numpy as np
from matplotlib import pyplot as plt
from time import time

def cheb_coeff(N,A,B):
	# CHEBCOEFF Generates coefficients of the Nth degree Chebyshev polynomial
	# Between A and B

	x			= np.cos((2.0*np.arange(1,N+1)-1)*np.pi/2.0/N)
	y			= np.sin(x*((B-A)/2)+(B+A)/2)
	T0			= np.zeros(N)
	T1			= np.ones(N)
	c			= np.append(np.sum(y)/N,np.zeros(N-1))
	a = 1
	for k in range(1,N):
		TL			= T1
		T1			= a*x*T1-T0
		T0			= TL
		c[k]		= np.sum(T1*y)*2.0/N
		a			= 2
	return c,x

def cheb_poly_eval(c,x):
	n	= c.shape[0]
	u	= c[n-1]*np.ones(x.shape)
	if n > 1:
		u_jp1	= u
		u		= c[n-2]+2.0*x*c[n-1]
		for j in range(n-3,-1,-1):
			u_jp2	= u_jp1
			u_jp1	= u
			u		= c[j]+2.0*x*u_jp1-u_jp2
		return u-x*u_jp1

def main():
	N	= 6			# Interpolation order-1
	A	= -np.pi		# Interval start
	B	= np.pi		# Interval end
	c,x	= cheb_coeff(N,A,B)
	Ntests	= 10
	Npts		= 1000
	xA			= np.linspace(A,B,Npts)
	timeTotal= 0

	# Transform to [-1,1]
	x	= (2*xA-A-B)/(B-A)

	for i in range(Ntests):
		t_s	= time()
		est	= cheb_poly_eval(c,x)
		ti	= (time()-t_s)
		timeTotal=timeTotal+ti
	cTime=timeTotal/Ntests

	timeTotal=0
	for i in range(Ntests):
		t_s	= time()
		y	= np.sin(xA)
		ti=time()-t_s
		timeTotal=timeTotal+ti
	sTime=timeTotal/Ntests

	#rmse=sqrt(sum((np.sin(x)-est).^2))/length(x)
	rmse=max(abs(np.sin(xA)-est))
	print('CTIME:%5.4f\tSTIME:%5.4f\tERROR:%5.4e'%(cTime,sTime,rmse))
	plt.plot(xA,np.sin(xA),label='Numpy')
	plt.plot(xA,est,label='Cheb')
	plt.legend()
	plt.grid()
	plt.show()
if __name__=="__main__":
	main()
