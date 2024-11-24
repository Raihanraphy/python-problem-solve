
'''
Task 
You are given an integer, NN, on a single line. The next line contains NN space-separated integers. Create a tuple, TT, of those NN integers, then compute and print the result of hash(TT).

Note: hash() is one of the functions in the __builtins__ module.

Input Format

The first line contains an integer, NN (the number of elements in the tuple). 
The second line contains NN space-separated integers describing TT.

Output Format

Print the result of hash(TT).

Sample Input

2
1 2
Sample Output

3713081631934410656
'''
#Map in Python is a function that works as an iterator to return a result after applying a function to every item of an iterable (tuple, lists, etc.).
#Map=(function, value[tuple, list etc]);

#A tuple is a finite, ordered list of elements that can be used in a variety of fields, including mathematics, computer programming, and database systems

#Code:
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))
