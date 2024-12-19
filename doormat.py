n,m=map(int,input().split())
s1='-'
s='.|.'
c=(m-3)//2
for i in range(0,n//2):
    print(s1*c+s*(2*i+1)+s1*c)
    c-=3
print(s1*((m-7)//2)+'WELCOME'+s1*((m-7)//2))
c=3
for i in range((n//2)-1,-1,-1):
    print(s1*c+s*(2*i+1)+s1*c)
    c+=3