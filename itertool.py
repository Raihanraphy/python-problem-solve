# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
str1, int1 = input().split()

for i in sorted(permutations(str1, int(int1))):
    print (''.join(i))