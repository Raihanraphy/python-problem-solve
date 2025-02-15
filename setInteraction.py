# Enter your code here. Read input from STDIN. Print output to STDOUT
e = input()
el = set(map(int,input().split()))
f = input()
fl = set(map(int,input().split()))

interset = el.intersection(fl)


print (len(interset))
