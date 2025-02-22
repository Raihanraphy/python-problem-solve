a = int(input())
b = list(map(int, input().split()))
c = int(input())
d = list(map(int, input().split()))

new=(set(b).symmetric_difference(set(d)))
print(len((new)))
