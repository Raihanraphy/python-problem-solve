import re

# using for loop
for i in range(int(input())):
    
    # using re.sub method and taking input
    s = re.sub("(?<=\s)&&(?=\s)", "and", input())
    
    #printing the required output
    print(re.sub("(?<=\s)\|\|(?=\s)", "or", s))
