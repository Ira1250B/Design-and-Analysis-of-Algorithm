def ln(n):
    count=0
    while(n>0):
        n//=10
        count+=1
    return count

def karatsuba(x,y):
    p=ln(x)
    q=ln(y)
    n=max(p,q)
    a=x//10**(n/2)
    b=x%10**(n/2)
    c=y//10**(n/2)
    d=y%10**(n/2)
    ac=a*c
    bd=b*d
    abcd=(a*d)+(b*c)
    
    return (ac*10**n+bd+abcd*10**(n/2))
x=1234
y=5678
print(karatsuba(x,y))

