# Strings

str1 = 'hello'
str2 = ' world'
bob = str1 + str2
print(bob)
#hello world

# looking inside strings 
# INDEXING

fruit = 'bannana'
letter = fruit[1]
print(letter)
#a
x = 3 
w = fruit[ x - 1]
print(w)
# n

# the build in function # len ( lenght ) will give us the length of a sting len ==> is a fuction 
print(len(fruit))
#7

# here i am using the variable fruit = 'bannana' unless i write a different variable 

index = 0 
while index < len(fruit):
  x = fruit[index]
  print(index, x)
  index = index + 1

#1- a2 n2 n3 a4 n5 a6 

for letter in fruit:
  print(letter)
  # this loop is more elegant 
# b a n n a n a 

# loops and counting 

word = 'bannana'
count = 0
for letter in word :
  if letter == 'a' :
    count = count + 1
print(count)
# 3

# syntax
"""
zot = 'abc'
print(zot[5])
# it would give syntax error cause the string zot only have 0-1-2 it don't have the index 5  
string out of range 

"""

# SLICING STRINGS

s = 'Monty python'
print(s[0:4])
# mont
print(s[6:7])
# p
print(s[6:20])
# python 

# the first no. is included while the second isn't included 
# also it is okay to refrence beyond the string index 
print(s[:2])
# Mo
print(s[8:])
# thon
print(s[:])
# Monty python