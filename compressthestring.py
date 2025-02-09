from itertools import groupby
for k, c in groupby(input()):
    print("(%d, %d)" % (len(list(c)), int(k)), end=' ')
