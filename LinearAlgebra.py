import numpy 
n = int(input().strip())
arr = numpy.array([input().strip().split() for _ in range(n)], dtype=numpy.float64) 
print(round(numpy.linalg.det(arr),2))
