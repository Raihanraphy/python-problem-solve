import numpy


a = input().split(' ')
b = tuple(map(int, a))

c = []
for i in range(b[0]):
    c.append(input().split(' '))
    
c = numpy.array(c, int)
print(numpy.transpose(c))
print(c.flatten())
