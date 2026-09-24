from scipy import special
x=10
j9= special.spherical_jn(9,x)
j10=special.spherical_jn(10,x)
j11=special.spherical_jn(11,x)

j11a=(21/x)*j10-j9
j9a=(21/x)*j10-j11

print(f"j11 upward=",j11a,"j11 normal=",j11,"difference",j11a-j11)
print(f"j9 upward=",j9a,"j9 normal=",j9,"difference",j9a-j9)
print("a=",(21/x)*j10)
print("j9=",j9)
print("j11=",j11)