
import numpy

n,m=tuple(map(int,input().split()))

print(str(numpy.eye(n, m,k=0)).replace('0',' 0').replace('1',' 1'))
