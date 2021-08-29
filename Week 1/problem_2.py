"""
Problem 2
10/10 Points

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcboboegghakl', then your program should print:

Number of times bob occurs is: 2
"""
count = 0
index = 0

for i in s:
    if s[index] == 'b' and index+3 <= len(s):
        if s[index+1] == 'o':
            if s[index+2] == 'b':
                count += 1
    index += 1

print('Number of times bob occurs is: ' + str(count))
