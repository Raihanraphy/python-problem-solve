# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
month, day, year = list(map(int,input().split()))
ans = calendar.weekday(year, month, day)
print((calendar.day_name[ans]).upper())
