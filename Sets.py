def average(array):
    # your code goes here
    my_set = set(array)
    avg = sum(my_set)/len(my_set)
    
    return (avg)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
