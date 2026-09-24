from scipy import special
from numpy import*
def bessel(l,x):
    res=zeros(l+1)
    lstart=l+int(sqrt(10*l))
    j2=0
    j1=1
    if(abs(x)<1e-30):
        res[0]=1
        return res
    if l==0:return res
    for i in range(lstart,0,-1):
        j0=((2*i+1)/x)*j1-j2
        if i-1<=l:
            res.append(j0)
        j2,j1=j1,j0
    res.reverse()
    true=sin(x)/x
    res=array(res)*(true/res[0])
    return res

l=10
x=0.1
dat0=special.spherical_jn(range(l+1),x)
dat1=bessel(l,x)
print("differece+:",dat0-dat1)


        

