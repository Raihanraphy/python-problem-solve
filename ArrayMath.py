import numpy as np
n,m=map(int,input().split())
a=np.empty(shape=(n,m),dtype=int)
b=np.empty(shape=(n,m),dtype=int)
for i in range(n):
    a[i]=input().split()
for i in range(n):
    b[i]=input().split()
print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(a//b)
print(np.mod(a,b))
print(np.power(a,b))
                        
