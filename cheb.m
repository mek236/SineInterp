clear all
close all


N=6;   % Interpolation order-1
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
    for j=N:-1:2;
        SV=DM1;
        DM1=2*x.*DM1-DM2+c(j);
        DM2=SV;
    end
    est=x.*DM1-DM2+0.5*c(1);

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
%rmse=sqrt(sum((sin(x)-est).^2))/length(x);
rmse=max(abs(sin(xA)-est));
plot(xA,sin(xA),xA,est)
fprintf('CTIME:%5.4f\tSTIME:%5.4f\tERROR:%5.4e\n',cTime,sTime,rmse)
