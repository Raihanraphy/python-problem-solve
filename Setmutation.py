# Set Mutations in python - Hacker Rank Solution
# python 3
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Set Mutations in python - Hacker Rank Solution START

len_set = int(input())

storage = set(map(int, input().split()))

op_len = int(input())

for i in range(op_len):
    operation = input().split()
    if operation[0] == 'intersection_update':
        temp_storage = set(map(int, input().split()))
        storage.intersection_update(temp_storage)
    elif operation[0] == 'update':
        temp_storage = set(map(int, input().split()))
        storage.update(temp_storage)
    elif operation[0] == 'symmetric_difference_update':
        temp_storage = set(map(int, input().split()))
        storage.symmetric_difference_update(temp_storage)
    elif operation[0] == 'difference_update':
        temp_storage = set(map(int, input().split()))
        storage.difference_update(temp_storage)
    else :
        assert False

print(sum(storage))
# Set Mutations in python - Hacker Rank Solution END