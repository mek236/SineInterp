clear all
close all


N=11;   % Interpolation order-1
A=0.0;  % Interval start
B=2*pi; % Interval end
c=chebcoeff(N,A,B);
Ntests=10;
Npts=1000000;
xA=linspace(0,2*pi,Npts);
timeTotal=0;

% Transform to [-1,1]
x=(2*xA-A-B)/(B-A);

for i=1:Ntests
    DM1=0;
    DM2=0;
    SV=0;
    tic
%    for j=N:-1:2;
%        SV=DM1;
%         DM1=2*x.*DM1-DM2+c(j);
%         DM2=SV;
%    end
%    est=x.*DM1-DM2+0.5*c(1);
%     est=c(1)+c(2)*x+c(3)*(x.*(4*x.*x-3))+...
%         c(4)*(1+x.*x.*(8-8*x.*x))+...
%         c(5)*(x.*(5+x.*x.*x.*(-20+16*x.*x)))+...
%         c(6)*(-1+x.*x.*(10-x.*x.*(-48+32*x.*x)))+...
%         c(7)*(x.*(-7+x.*x.*x.*(40-x.*x.*(-112+x*64))));
	%est=c(1)-c(3)-c(5)+x.*(c(2)-3*c(4)+x.*(2*c(3)-8*c(5)+x.*(4*c(4)+x.*8*c(5))));
	est=c(1)-c(3)+c(5)-c(7)+c(9)-c(11)+...
		x.*(c(2)-3*c(4)+5*c(6)-7*c(8)+9*c(10)+...
		x.*(2*c(3)-8*c(5)+10*c(7)-24*c(9)+42*c(11)+...
		x.*(4*c(4)-20*c(6)+40*c(8)-88*c(10)+...
		x.*(8*c(5)-48*c(7)-128*c(9)-304*c(11)+...
		x.*(16*c(6)-112*c(8)+368*c(10)+...
		x.*(32*c(7)-256*c(9)+992*c(11)+...
		x.*(64*c(8)-576*c(10)+...
		x.*(128*c(9)-1280*c(11)+...
		x.*(256*c(10)+...
		x.*(512*c(11)))))))))));
    timeI=toc;
    timeTotal=timeTotal+timeI;
end
cTime=timeTotal/Ntests;

timeTotal=0;
for i=1:Ntests
    tic
    y=sin(xA);
    ti=toc;
    timeTotal=timeTotal+ti;
end
sTime=timeTotal/Ntests;
rmse=sqrt(sum((sin(x)-est).^2))/length(x);
disp(sprintf('CTIME:%5.4f\tSTIME:%5.4f\tERROR:%5.4e\n',cTime,sTime,rmse))
