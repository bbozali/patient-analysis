""" This module counts the numbers of lines in standart input
Input: string from the system standard input
"""



import sys

count=0
for line in sys.stdin:
    count +=1

print(count, 'lines in standard output')
