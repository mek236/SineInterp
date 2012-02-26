function [ c ] = chebcoeff( N,A,B )
%CHEBCOEFF Generates coefficients of the Nth degree Chebyshev polynomial
% Between A and B

    k=1:N;
    Y=cos(pi*(k-.5)/N);
    F=sin(Y*((B-A)/2)+(B+A)/2);
    c=zeros(N,1);
    for j=1:N
        sum=0.0;
        for i=1:N
            sum=sum+F(i)*cos((pi*(j-1))*((i-0.5)/N));
        end
        c(j)=sum*(2/N);
    end
end

