from collections import defaultdict
input_n, input_m = map(int, input().split())
d = defaultdict(list)
for i in range(input_n):
    ans1 = input()
    d[ans1].append(i+1)
for j in range(input_m):
    ans2 = input()
    if ans2 in d:
        print(*d[ans2])
    else:
        print(-1)
