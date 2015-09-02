import numpy as np
from matplotlib import pyplot as plt
from time import time

def cheb_coeff(N,A,B):
	# CHEBCOEFF Generates coefficients of the Nth degree Chebyshev polynomial
	# Between A and B 
	k	= np.arange(N)*1.0
	Y	= np.cos(np.pi*(k-0.5)/N)
	F	= np.sin(Y*((B-A)/2.0)+(B+A)/2.0)
	c	= np.zeros(N)
	for j in range(N):
		csum=0.0
		for i in range(N):
			csum=csum+F[i]*np.cos((np.pi*(j-1))*((i-0.5)/N))
		c[j]=csum*(2.0/N)
	return c

def main():
	N	= 10			# Interpolation order-1
	A	= 0			# Interval start
	B	= np.pi		# Interval end
	c	= cheb_coeff(N,A,B)

	Ntests	= 10
	Npts		= 10
	xA			= np.linspace(A,B,Npts)
	timeTotal= 0

	# Transform to [-1,1]
	x	= (2*xA-A-B)/(B-A)

	for i in range(Ntests):
		DM1=0.0
		DM2=0.0
		SV	=0.0
		t_s	= time()
		for j in range(N-1,0,-1):
			SV		= DM1
			DM1	= 2.0*x*DM1-DM2+c[j]
			DM2	= SV
		est	= x*DM1-DM2+0.5*c[0]
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
