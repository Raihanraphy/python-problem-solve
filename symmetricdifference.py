n1 = int(input())
set_a = set(map(int,input().split()))
n2 = int(input())
set_b = set(map(int,input().split()))
a = (set_a.difference(set_b))
b = (set_b.difference(set_a))
ans = a.union(b)
for i in sorted(ans):
        print (i)
