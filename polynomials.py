import numpy

P = list(map(float, input().split()))
print(numpy.polyval(P, int(input())))
