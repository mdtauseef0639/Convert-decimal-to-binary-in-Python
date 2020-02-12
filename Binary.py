a=[]
n=int(input())
if n==0:
    print(0)
elif n==0:
    print(1)
else:
    while n!=1:
        rem=n%2
        n=n//2
        a.append(rem)
    
    a.append(n)
a=a[::-1]



res = sum(d * 10**i for i, d in enumerate(a[::-1]))
print(res)
