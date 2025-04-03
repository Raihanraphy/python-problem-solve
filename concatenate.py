
import numpy

n,m,p=map(int,input().split())

lista1=[list(map(int,input().split())) for i in range(n)]
lista2=[list(map(int,input().split())) for i in range(m)]
a1=numpy.array(lista1)
a2=numpy.array(lista2)

print(numpy.concatenate((a1,a2),axis=0))
