"""
String Formatting
Given an integer, , print the following values for each integer  from  to :

1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary

Function Description

Complete the print_formatted function in the editor below.

print_formatted has the following parameters:

int number: the maximum value to print
Prints

The four values must be printed on a single line in the order specified above for each i from 1 to number . 
Each value should be space-padded to match the width of the binary value of number and the values should be separated by a single space.

Input Format
A single integer denoting n.

Constraints

1<n<99 """
def print_formatted(number):
    # your code goes here
    for i in range(1, number + 1):
        # Calculate the width based on the binary representation of the input number
        binary = len('{0:b}'.format(number))
        length = int(binary)
        # Print the number in decimal, octal, hexadecimal, and binary formats
        print('{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(i, width=length))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)