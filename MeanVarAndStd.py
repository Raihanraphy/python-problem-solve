from numpy import array, mean, var, std

arr = []
n, m = map(int, input().split())

for _ in range(n):
    arr.append([*map(int, input().split())])
arr = array(arr)

print(mean(arr, axis=1))
print(var(arr, axis=0))
print(round(std(arr), 11))
