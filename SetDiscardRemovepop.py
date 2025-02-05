input()
s  = list(map(int, input().split()))
s.reverse()
s = set(s)
num_commands = int(input())
command = ["", ""]
for i in range(num_commands):
    command = input().split()
    if len(command) == 1:
        getattr(s, command[0])()
    elif len(command) == 2:
        command[1] = int(command[1])
        if command[1] in s:
            getattr(s, command[0])(command[1])
print(sum(s))
