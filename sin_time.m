clear all
close all
% Time sin
x=linspace(0,2*pi,1e6);
N=100;
sinTotal=0;
sinVar=0;
for n=1:N
	tic
	y=sin(x);
	yT=toc;
	sinTotal=sinTotal+yT;
	sinVar=sinVar+yT^2;
end
AVGSIN=sinTotal/N;
VARSIN=(sinVar-AVGSIN^2)/(N-1);

sqTotal=0;
sqVar=0;
for n=1:N
	tic	
	z=x.*x;
	zT=toc;
	sqTotal=sqTotal+zT;
	sqVar=sqVar+zT^2;
end
AVGSQ=sqTotal/N;
VARSQ=(sqVar-AVGSQ^2)/(N-1);

fprintf('\nFor %i iterations \n FUNCTION \tAVG\tVAR\nSIN(x)\t%f4\t%f4\nX^2\t%f4\t%f4\n',N,AVGSIN,VARSIN,AVGSQ,VARSQ); 
