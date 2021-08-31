"""
Problem 3
15/15 Points

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters
occur in alphabetical order. For example, if s = "azcboboegghakl", then
your program should print:

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = "abcbcd",
then your program should print:

Longest substring in alphabetical order is: abc
"""
temp_longest = ''
longest = ''
alpha = 'abcdefghijklmnopqrstuvwxyz'
new_index = 0    # pointer for possible alpha chain
old_index = 0

for x in s:
    new_index = alpha.find(x)
    if alpha.find(alpha[new_index]) >= alpha.find(alpha[old_index]):
        temp_longest += x
    else:
        temp_longest = x
    old_index = new_index
    if len(temp_longest) > len(longest):
        longest = temp_longest

print("Longest substring in alphabetical order is: " + longest)
