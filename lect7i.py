from scipy import*
from numpy import *
def bessel(l,x):
    result=zeros(l+1)
    if(abs(x)<1e-30):
        result[0]=1
        return result
    j0=sin(x)/x
    result[0]=j0
    if l==0: return result
    j1=j0/x-cos(x)/x
    result[1]=j1
    for i in range(1,l):
        j2= ((2*i-1)/x)*j1 - j0
        result[i+1]=j2
        j0,j1=j1,j2
    return result
l=10
x=0.1
dat1=bessel(l,x)
print(dat1)


 