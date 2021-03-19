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

#sting manipulating 
# if we want a space betwen sting when we use the + operator we add " "
# + when it is added to strings it means ' concatenation ' it concationate the stiring with no space
# in is like == if like
'n' in fruit 
'm' in fruit
'nan' in fruit
#her in is ask if nan is in fruit and fruit is bannana means it ask if nan is in bannana the answer is either true of False

if word == 'bannana':
  print('all right, bannana')
if word < 'bannana':
  print('your word,' + word + ", comes after bannana")
elif word > 'bannana':
  print('your word,' + word + ", comes after bannana")
else:
  print('all right, bannana')
  
# all right bannana

# == compares character for character \ upper case letter is < small case letter 
great = 'HELLO Bob'
zap = great.lower()
#here it say to make a copy of great that is lower case and it don't change the original that is great
print(zap)
#hello bob
print('Hi There'.lower())
# hi there 
# lower is a build in 'OBJECT METHOD' THIS THING IS A METHOD

# THIS IS A THING THAT IS OF A CATAGORY STING = class
# TYPE GIVE THAT TYPE OF DATA U INTER 
#DIR GIVES THE STUFF U CAN DO WITH THE TYPE OF DATA U ENTERED 'WHAT IS THE DATA CAPPABLE OF ' = IT IS METHOD IN THE CLASS 
""" 

SOME OF THE STING LYBRARY
str.capotalize() --> make the string capital
str.center(width[, fillchar]
str,endswith(suffix[, star[, end]])
str.find(sub[, start[, end]] --> looks for stuff in the string 
str.lstrip([chars])
str.replace(old, new[, count]) 
str,lower()
str.rstrip([chars])
str.strip([chars])
str.upper()

"""
pos = fruit.find('na')
print(pos)
##2
# it will find the letter and give me where it is located in numbers
aa = fruit.find('z')
print(aa)
##-1 cause it is not there in the string 

greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
# here it says replace Jane with Bob and if there is more thab 1 bob it will replace all of them with jane
print(nstr)
## Hello Jane 

greeet = '   Hello bob'
greeet.lstrip()# --> STRIP SPACE FROM LEFT SIDE 
## 'Hello bob   '
greeet.rstrip()
## '   Hello bob' # --> STRIP SPACE FROM RIGHT SIDE 
greeet.strip() # --> REMOVE THE SPACES FROM RIGHT AND LEFT
## 'Hello bob'

# THE ORIGINAL STRING WILL STARY IT WILL MAKE  A NEW COPY AND APPLY THE CHANGES ON IT 

line = 'Please have a nice day'
line.startswith('Please')
## true
line.startswith('p')
## False
# her we can check it the string starts with like we can use it in if statement like to say if the sting that start with something : do with it this and so on

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atops = data.find('@')
print(atops)
## 21
sppos = data.find(' ', atops)
# her we write the 'atops' to tell python to start searching from the @ character
print(sppos)
## 31
host = data[atops+1 : sppos]
# we say one beyond the @ which is 'u' to the space posision but not including it which is the 'a'
print(host)
##uct.ac.za



#FILES WE WILL BE PLAYING WITH inbox.TXT FILES 
# this is just a flat text file that python is able to read 
#first before we use a file we tell python that we r going to use it by useing open

"""
handle = open(filename, mode ) --> fhand = open('mbox.txt', 'r') -- her we told python the name of the
file and told him that we r only going to read it cause we use 'r'  her it give handle it isn't the data but someting that we can manipulate it is like a port between the program and the file that is open 
we can read or write  it is telling us something but it is not that actual file 
if we try to open a file that doesn't work or exsit the it will give a trace back
return a handle use to manipulate the file
the file name is a string 
mode is Optional and should be 'r' if we are planning to read the file and 'w' if we are going to write to the file
"""
#\n --> it is not 2 character it is just a single character that move the thing next it to the next line n\ is resembled as 1 character in python not 2
stuff = 'Hello\nWorld!'
##Hello 
##world
print(stuff)
stuff = 'X\nY;
print(stuff)
## x
## Y
len(stuff)
## 3 
# it is 3 cause X is a char and \n is a char and Y is a char and that is 3 characters not 4 


#\n == newlines --> it is like the Enter Botton in windows it work exacty like it 
# when print is excuted it will have a line after it 

xfile = open('mbox.txt')
for cheese in xfile:
  print(cheese)

# a file handle that is in this case 'xfile' open for read can be treated as a sequence of strings where each line in the file is a strings in the sequence
# we can use thr for statement to iterate through a sequence 
# remember a sequence is an ordered set

fhand = open('mbox.txt')
count = 0 
for line in fhand:
  count = count + 1 
print('Line Count:', count)
## LIne Count: 132045

inp = fhand.read()
# her we will read the whole thing the whole file(newlines & all) into a single string unlike the ubove it will gp through each line indivisually
print(len(inp))
## 94626 --> this is the character numbers 
print(inp[:20])
## From stephen.marquar
# when we print we will se the newlines here it will read the whole things

for line in fhand