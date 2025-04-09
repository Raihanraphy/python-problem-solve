# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

N_M = list(map(int, input().split()))
a = numpy.array([list(map(int, input().split())) for i in range(N_M[0])])
print(numpy.prod(numpy.sum(a, axis = 0)))
