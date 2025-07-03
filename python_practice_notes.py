x = input('Enter some value: ')
print(type(x))  # it is always str type

x = input('Enter First Number: ')
y = input('Enter Second Number: ')
i = int(x)
j = int(y)
print('The Sum: ', i + j)

x = int(input('Enter First Number: '))
y = int(input('Enter Second Number: '))
print('The Sum:', x + y)

print('The Sum:', int(input('Enter First Number:')) + int(input('Enter Second Number: ')))

# Q. Write a program to read Employee data from the keyboard and print that data to the console?
# eno, ename, esal, eaddr
# eno --> int
# ename --> str
# esal --> float
# eaddr --> str

eno = int(input('Enter Employee Number: '))
ename = input('Enter Employee Name: ')
esal = float(input('Enter Employee Salary: '))
eaddr = input('Enter Employee Address: ')
married = bool(input('Employee Married?[True|False]: '))
print('Please confirm your information:')
print('Employee Number:', eno)
print('Employee Name:', ename)
print('Employee Salary:', esal)
print('Employee Address:', eaddr)
print('Employee Married?:', married)

# **********py test.py
# Enter Employee Number: 872425
# Enter Employee Name: Durga
# Enter Employee Salary: 70000
# Enter Employee Address: Hyd
# Employee Married?[True|False]: False
# Please confirm your information:
# Employee Number: 872425
# Employee Name: Durga
# Employee Salary: 70000.0
# Employee Address: Hyd
# Employee Married?: False

eno = eval(input('Enter Employee Number: '))
ename = input('Enter Employee Name: ')
esal = eval(input('Enter Employee Salary: '))
eaddr = input('Enter Employee Address: ')
married = eval(input('Employee Married?[True|False]: '))
print('Please confirm your information:')
print('Employee Number:', eno)
print('Employee Name:', ename)
print('Employee Salary:', esal)
print('Employee Address:', eaddr)
print('Employee Married?:', married)

x = eval(input('Enter some value:'))
y = eval(input('Enter some value:'))
print(x + y)

x = eval(input('Enter Some Expression:'))
print(x)

x = eval(input('Enter Some Value:'))
print(type(x))
print(x)

# x = eval(10.5)  # error

# eval() is always taking string argument only, but that string should represent some valid non-string value internally.

x = eval('10')  # Example: eval('10') returns int 10
print(type(x))
print(x)

s = '10 20 30'
l = s.split()
print(l)  # ['10', '20', '30']
# [10, 20, 30]
# string value to int type ===> int()
a, b, c = [10, 20, 30]
print(a, b, c)  # unpacking

s = input('Enter Two Numbers: ')
l = s.split()
print(l)  # ['10', '20']

a, b = input('Enter Two Numbers: ').split()
print(a, b)

a, b = [int(x) for x in input('Enter Two Numbers: ').split()]  # for each string present in this list, convert into int value # list comprehension
print('The Product:', a * b)

a, b = [int(x) for x in input('Enter 2 int values: ').split()]
print('The Product:', a * b)

a, b = [int(x) for x in input('Enter 2 int values: ').split(',')]
print('The Product:', a * b)

from sys import argv
print('The Number of Command Line arguments:', len(argv))
print('The List of Command Line arguments:', argv)
print('First argument:', argv[0])
print('Second argument:', argv[1])
for x in argv:
    print(x)

from sys import argv
x = argv[1:]  # ['10', '20', '30']
sum = 0
for x1 in x:
    n = int(x1)
    sum = sum + n
    # sum = n
print('The Sum:', sum)

from sys import argv
print(int(argv[1]) + int(argv[2]))

# from sys import argv
# print(argv[10])  # Potential IndexError

# 1. space is the separator. If we should use ""
# 2. always str type - typecasting
# 3. out of range index - IndexError

-------------------------------------


a, b, c = 10, 20, 30
print(a, b, c, sep='=')  # 10=20=30

print('Hello', end='***')
print('durga')  # Hello***durga

a, b, c = 10, 20, 30
print(a, b, c, sep='*')
print(a, b, c, sep='-')

a, b, c = 10, 20, 30
print(a, b, c, sep='**', end='###')
print(a, b, c, sep='-')
print('durga')

a, b, c = 10, 20, 30
print(a, b, c, sep='\n', end='###')
print(a, b, c, sep='-')
print('durga', end='')

x = 5
y = 10
print(f"{x} + {y} = {x + y}")  


name = "Aman"
age = 28
print(f"Hi {name},what is your age ,is it {age}?")  




name = input('Enter Your Name: ')
if name == 'durga':
    print('Hello Durga Good Morning!!!')
print('How are you')

name = input('Enter Your Name: ')
if name == 'durga':
    print('Hello Durga, Good Morning')
else:
    print('Hello Guest, Good Morning')
print('How are you')



n1 = int(input('Enter First Number: '))
n2 = int(input('Enter Second Number: '))
if n1 > n2:
    print('Biggest Number:', n1)
else:
    print('Biggest Number:', n2)

n1 = int(input('Enter First Number: '))
n2 = int(input('Enter Second Number: '))
n3 = int(input('Enter Third Number: '))
if n1 > n2 and n1 > n3:
    print('Biggest Number:', n1)
elif n2 > n3:
    print('Biggest Number:', n2)
else:
    print('Biggest Number:', n3)


# IPL Fan Team Selector
chosen_team = input('Select Your IPL Team for the Match: ')

if chosen_team == 'RCB':
    print("Royal Challengers Bangalore (RCB) - The team with the most passionate fans!")
elif chosen_team == 'MI':
    print("Mumbai Indians (MI) - The champions with a legacy of success!")
elif chosen_team == 'CSK':
    print("Chennai Super Kings (CSK) - The team with the coolest captain!")
else:
    print("Other teams are not recommended in this IPL season!")
    
    
# Q. Write a program to find smallest of given 2 numbers?
# Q. Write a program to find smallest of given 3 numbers?
# Q. Write a program to check whether the given number is even or odd?
# Q. Write a program to check whether the given number is in between 1 and 100 (inclusive)?

n = int(input('Enter a digit from 0 to 9: '))
if n == 0:
    print('ZERO')
elif n == 1:
    print('ONE')
elif n == 2:
    print('TWO')
elif n == 3:
    print('THREE')
elif n == 4:
    print('FOUR')
elif n == 5:
    print('FIVE')
elif n == 6:
    print('SIX')
elif n == 7:
    print('SEVEN')
elif n == 8:
    print('EIGHT')
elif n == 9:
    print('NINE')
else:
    print('Please enter a digit from 0 to 9')


s = input('Enter Any String: ')
i = 0
for ch in s:
    print('The character present at', i, 'index:', ch)
    i = i + 1  # i += 1

for x in range(1, 11):
    print(x, 'Hello')

for x in range(21):
    if x % 2 != 0:
        print(x)

for x in range(1, 21, 2):
    print(x)

# To print the sum of numbers present in the given list???
# [10,20,30,40] ===> 100

l = eval(input('Enter List: '))  # [10,20,30,40]
sum = 0
for x in l:
    sum = sum + x
print('The Sum:', sum)

# reading input by using input() function and command line arguments???
# input() ===> To read data from the end user
# command line arguments ==> input provided by the person who is executing our program

l = input('Enter List: ')
sum = ''
for x in l:
    sum = sum + x
print('The Sum:', sum)

# Enter List: ['a', 'b','c']
# The Sum: abc
# Enter List: ['a', 'b','c']
# The Sum: ['a', 'b', 'c']
# **********

x = 1
while x <= 10:
    print(x)
    x = x + 1
for i in range(1, 11):
    print(i)

# To print numbers from 1 to 10 by using while loop????
# To display the sum of first n natural numbers??

n = int(input('Enter n value: '))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i + 1
print('The sum of first {} numbers: {}'.format(n, sum))

sum = 0
for x in range(1, n + 1):
    sum = sum + x
print(sum)

name = ''
while name != 'aman':
    name = input('Enter Your Favourite Heroine: ')
print('Thanks for confirmation')

name = ''
i = 0
while name != 'aman':
    name = input('Enter Your Favourite Heroine: ')
    i = i + 1
    if i == 10:
        print("Your Maximum attempts completed")
        break

i = 0  #  do not execute infinite loop
while True:
    i = i + 1
    print('The Current Count:', i)

for i in range(4):
    for j in range(4):
        print(i, j)

while True:
    username = input('Enter User Name: ')
    pwd = input('Enter Password: ')
    if username == 'durga' and pwd == 'sunny':
        print('You are valid user, you can avail services')
        break
    else:
        print('Your credentials are invalid, please provide again')




for i in range(10):
    if i == 7:
        break
    print(i)
print('Loop execution enough...plz break')

cart = [10, 20, 600, 60, 70]
for item in cart:
    if item > 500:
        break
    print(item)
print('To place this order, insurance must be required')

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

cart = [10, 20, 500, 700, 50, 60]
for item in cart:
    if item >= 500:
        continue
    print('Processing Item:', item)
    print('We cannot process this item because of insurance issue:', item)

cart = [10, 20, 500, 700, 50, 60]
for item in cart:
    if item >= 500:
        break
    print('Processing Item:', item)
    print('We cannot process this item because of insurance issue:', item)

numbers = [10, 20, 0, 5, 0, 30]
for n in numbers:
    if n == 0:
        continue
    print('100 / {} = {}'.format(n, 100 / n))
    print('Hello Stupid, How we can divide with zero. just skipping')

cart = [10, 20, 30, 40, 50]
for item in cart:
    if item >= 500:
        print('We cannot place this order')
        break
    print('Processing item:', item)
else:
    print('Congrats... All your items processed successfully')

# with continue

# Q1. What is the difference between for loop and while loop???
# Repeat code for every item in the sequence ---> for loop
# Repeat code as long as some condition is True ---> while loop
# Q2. How to exit from the loop?
# break statement
# Q3. How to skip some iterations inside loop?
# continue statement
# Q4. When else part will be executed for loops?
# if the loop without break then only else will be executed.

if 10 > 20:
    print('Hello')
else:
    pass

def additem():
    pass
def deleteitem():
    pass
def updateitem():
    print('Updating item implementation')

x = 10
del x
# print(x)  # NameError: name 'x' is not defined

s1 = 'durga'
s2 = s1
s3 = s1
del s1
print(s2)
print(s3)

s1 = 'durga'
del s1
# print(s1)  # NameError: name 's1' is not defined
s1 = 'durga'
s1 = None
print(s1)

s1 = 'durga'
# del s1[0]  # TypeError: 'str' object doesn't support item deletion

# pass ===> empty statement
# del ===> to delete variables which are no longer required in our program
# automatically the corresponding objects eligible for gc.
# if useless objects deleted, free memory will be improved.
# our program won't face memory issues.

s = 'The classes of \'Python\' By \"Durga Sir\" are Good'
s = '''The classes of 'Python' By "Durga Sir" are Good'''
print(s)

# ''' sdjfklsjad '''
# sdflsjdfkls ''''
# 1. To define multiline string literals
# 2. To use single or double quotes as symbol only
# 3. Doc string

# How to access characters of the string:
# 2 ways
# 1. By using index
# 2. By using Slice Operator

# Q. Write a program to read string from the keyboard and display its characters by index wise (both positive index and negative index)???

s = input('Enter Any String: ')
i = 0
for x in s:
    print('The Character Present at Positive Index {} is : {}'.format(i, x))
    i = i + 1

s = input('Enter Any String: ')
i = 0
for x in s:
    print('The Character Present at Positive Index {} and at Negative Index {} is : {}'.format(i, i - len(s), x))
    i = i + 1

s = 'Learning Python is very easy'
print(s[1:5])

# print(s[1:7])  # earning
# s[:7]  # Learning
# s[1:]  # earning Python is very easy
# s[:]  # Learning Python is very easy
# s[1:7:1]  # earning

s = 'abcdefghijklmnopqrstuvwxyz'
print(s[1:15:1])  # bcdefghijklmno
print(s[1:15:3])  # behk

# 2. By using Slice Operator:
# [begin_index:end_index:step]
# [begin:end:step]
# [begin:end]
# from begin index to end-1 index
# for begin and end we can take either positive index or negative index.

s = 'abcdefghijklmnopqrstuvwxyz'
print(s[1:10000:1])  # bcdefghijklmnopqrstuvwxyz
# Slice Operator won't raise IndexError

s = 'abcdefghijklmnopqrstuvwxyz'
print(s[11000:1000:1])  # empty string

# [begin:end]
# from begin index to end-1 index
# for begin and end we can take either positive index or negative index
# step value can be either positive or negative.
# The default step value is: +1
# +ve step value means forward direction (left to right)
# from begin to end-1
# -ve step value means backward direction (right to left)
# from begin to end+1

s = 'abcdefghijklmnopqrstuvwxyz'
print(s[::-1])  # zyxwvutsrqponmlkjihgfedcba
# reverse string

# In Forward Direction:
# default begin value: 0
# default end value: len(s)
# default step value: 1
# In Backward Direction:
# default begin value: -1
# default end value: -len(s)-1

s = 'abcdefghijklmnopqrstuvwxyz'
print(s[::-1])  # zyxwvutsrqponmlkjihgfedcba
print(s[-1:-27:-1])  # zyxwvutsrqponmlkjihgfedcba
# default begin: -1
# default end: -26-1=-27

# In the forward direction if end value is 0 then result is always empty.
# In the backward direction if end value is -1 then result is always empty.

# s[begin:end:step]
# all attributes are optional
# All values can be either positive or negative
# if step is +ve then forward direction from begin to end-1
# if step is -ve then backward direction from begin to end+1
# In forward direction if end is 0 then result is always empty string.
# In backward direction if end is -1 then result is always empty string.

# s[::0]  # error, step cannot be zero

s = 'abcdefghij'
print(s[1:6:2])  # bdf

s = 'abcdefghij'
# s[1:6:2] ---> forward direction, begin to end-1 (1 to 5)

# >>> s[1:6:2]
# 'bdf'
# >>> s[::1]
# 'abcdefghij'
# >>> s[::-1]
# 'jihgfedcba'
# >>> s[3:7:-1]  # empty string

# s[1:6:2] ---> forward direction, begin to end-1 (1 to 5)
# s[::1] ---> complete string in original order
# s[::-1] ---> complete string in reverse order
# s[3:7:-1] ---> backward direction, from begin to end+1 (3 to 8)

s = 'abcdefghij'
# s[1:6:2] ---> 'bdf'
# s[::1] ---> 'abcdefghij'
# s[::-1] ---> 'jihgfedcba'
# s[3:7:-1] ---> '' (empty)
# s[7:4:-1] ---> 'hgf'
# s[0:10000:1] ---> 'abcdefghij'
# s[0:10000:-1] ---> '' (empty)
# from 0 to 10000
# s[-4:1:-1] ---> 'gfedc'

# Write a program to read string from the keyboard and print its characters in both forward and backward direction??

s = input('Enter Any String: ')
print('In Forward Direction:')
i = 0
n = len(s)
while i < n:
    print(s[i])
    i = i + 1
print('In Backward Direction:')
i = -1
while i >= -len(s):
    print(s[i])
    i = i - 1

s = input('Enter Any String: ')
print('In Forward Direction:')
for x in s:
    print(x)
print('In Backward Direction:')
for x in s[::-1]:
    print(x)

# string comparison

s1 = input('Enter First String: ')
s2 = input('Enter Second String: ')
if s1 == s2:
    print('Both Strings are equal')
elif s1 < s2:
    print('First String is less than Second String')
else:
    print('First String is greater than Second String')

city = input('Enter Your City Name: ')
if city == 'Hyderabad':
    print('Hello Hyderabadi.. Aadaab')
elif city == 'Chennai':
    print('Hello Madrasi...Vanakkam')
elif city == 'Bangalore':
    print('Hello Kannadiga.. Namaskara')
else:
    print('Your Entered City', city, 'is invalid')

# Remove Spaces from the strings:
# rstrip() ---> To remove spaces at right hand side (end of string)
# lstrip() --> left hand side (beginning of the string)
# strip() --> To remove both sides

city = input('Enter Your City Name: ').strip().lower()
if city == 'hyderabad':
    print('Hello Hyderabadi.. Aadaab')
elif city == 'chennai':
    print('Hello Madrasi...Vanakkam')
elif city == 'bangalore':
    print('Hello Kannadiga.. Namaskara')
else:
    print('Your Entered City', city, 'is invalid')

city = input('Enter Your City Name: ')
scity = city.strip()
if scity == 'Hyderabad':
    print('Hello Hyderabadi.. Aadaab')
elif scity == 'Chennai':
    print('Hello Madrasi...Vanakkam')
elif scity == 'Bangalore':
    print('Hello Kannadiga.. Namaskara')
else:
    print('Your Entered City', city, 'is invalid')

# Finding substrings:
# find()
# index()
# rfind()
# rindex()
# string.find(substring)
# Returns index of first occurrence of the given substring.
# Returns -1 if it is not available.

s = 'Learning Python is very python easy'
print(s.find('Python'))  # 9
print(s.find('java'))    # -1
print(s.find('r'))       # 2

print(s.rfind('python'))  # 23

s = 'Learning Python is very easy'
print(s.find('Python', 15, 25))  # -1
print(s.rfind('Python'))         # 9

# find(substring, begin, end)
# from begin to end-1
# 15 to 24

s = 'Learning Python is very easy'
print(s.find('v', 15, 25))  # 21

# s.find(substring)
# s.find(substring, begin, end)

s = 'aaaaaaaaaabbbbaaaaaabaaaaaaa'
print(s.find('a'))  # 0

s = 'aaaabbbbbbaaaaabbbbbbbbb'
print(s.find('a'))    # 0
print(s.rfind('a'))   # 15

s = 'aaaabbbbbbaaaaabbbbbbbbb'
print(s.find('a'))         # 0
print(s.rfind('a'))        # 15
print(s.find('a', 5, 20))  # 11
print(s.rfind('a', 5, 20)) # 15

# Finding the substrings:
# find(substring)
# find(substring, begin, end)
# rfind(substring)
# rfind(substring, begin, end)
# index(substring)
# index(substring, begin, end)
# rindex(substring)
# rindex(substring, begin, end)

s = 'Learning python is very easy'
print(s.find('p'))    # 9
print(s.rfind('y'))   # 27

# find(substring)
# if the specified substring not present it returns -1

# index() method is exactly same as find() method except that if the specified substring is not available then we will get ValueError.

s = 'Learning python is very easy'
print(s.find('p'))    # 9
print(s.rfind('y'))   # 27
print(s.index('p'))   # 9
print(s.rindex('y'))  # 27
# print(s.index('z'))  # ValueError: substring not found
# to Check

# Program to display all positions of the substring in the given main string???
# main string: 'aadkfjsabdz'
# substring: 'a'
# Found at index: 0
# Found at index: 1
# Found at index: 8
# The total number of occurrences: 3

# aaaabdabdaba
# ab
# n = len(s)  # 7, 2
# pos = 0
# i = s.find(subs, pos, n)
# print('Found at index:', i)  # 3
# s.find(subs, i + len(subs), n)

s = input('Enter Main String: ')
subs = input('Enter sub String: ')
n = len(s)
pos = 0
while True:
    i = s.find(subs, pos, n)
    if i == -1:
        break
    else:
        print('Found at index:', i)
        pos = i + len(subs)

s = input('Enter Main String: ')
subs = input('Enter sub String: ')
n = len(s)
pos = 0
count = 0
while True:
    i = s.find(subs, pos, n)
    if i == -1:
        break
    else:
        print('Found at index:', i)
        count += 1
        pos = i + len(subs)
print('The Total Number of Occurrences:', count)

s = input('Enter Main String: ')
subs = input('Enter sub String: ')
print('The Total Number of Occurrences:', s.count(subs))
print('The Total Number of Occurrences:', s.count(subs, 4, 10))

s = 'Learning Python is very difficult'
s1 = s.replace('difficult', 'easy')
print(s1)

s = 'abababababab'
s1 = s.replace('a', 'b')
print(s1)

# Write a script to find the number of spaces present in the given string?

s = ' aba bab aba ba b '
s1 = s.replace(' ', '')
print(s)
print(s1)

s = ' aba bab aba ba b '
s1 = s.replace(' ', '')
print(len(s) - len(s1))

# string is immutable, how replace() method works.

s = 'durga software solutions'
l = s.split()
for x in l:
    print(x)

s = 'one, two, three, four, five'
l = s.split(',')
for x in l:
    print(x)

s = '01-08-2020'
l = s.split('-')
for x in l:
    print(x)

# joining of strings:
# a group of strings (list or tuple) can be joined by using the given delimiter.
# l = s.split(separator)
# s = separator.join(l)

l = ['sunny', 'bunny', 'chinny']
s = ' '.join(l)
print(s)

t = ('10', '20', '30')
s = ' '.join(t)
print(s)

# Changing case of a string?
# 1. upper() ---> Every lower case character will be converted into uppercase
# 2. lower() ---> Every upper case character will be converted into lower case
# 3. swapcase() ===> lower --> upper and upper --> lower
# 4. title() ===>
# 5. capitalize() ===>

s = 'learning PYTHON is very easy'
print(s.upper())

s = 'learning PYTHON is very easy'
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize())

# To check type of characters present in the given strings

# 1. isalnum() ---> a to z, A to Z, 0 to 9
# 2. isalpha() ---> a to z, A to Z
# 3. isdigit() ---> 0 to 9
# 4. islower() ---> If every alphabet symbol is in lower case
# 5. isupper() ---> If every alphabet symbol is in upper case
# 6. istitle() ---> If the string is in title case
# 7. isspace() ---> If the string contains only spaces

print('Durga786'.isalnum())       # True
print('durga786'.isalpha())       # False
print('DurgA'.isalpha())          # True
print('123456'.isdigit())         # True
print('durga'.islower())          # True
print('Durga'.islower())          # False
print('durga123'.islower())       # True

print('ABC123'.isupper())         # False
print('Learning Python is very easy'.istitle())  # False
print('Learning Python Is Very Easy'.istitle())  # True
print(' '.isspace())              # True
print('a b c d'.isspace())        # False

print('Durga'.isalpha())          # True

s = input('Enter Any Character: ')
if s.isalnum():
    print('Alpha Numeric Character')
    if s.isalpha():
        print('Alphabet character')
        if s.islower():
            print('Lower case Alphabet Character')
        else:
            print('Upper case alphabet Character')
    else:
        print('It is a digit')
elif s.isspace():
    print('It is Space character')
else:
    print('Non Space special Character')

s = 'learning python is very easy'
print(s.startswith('l'))               # True
print(s.startswith('learning python')) # True
print(s.endswith('learning python'))   # False
print(s.endswith('easy'))              # True
# print(s.endswith('very easy'))       # False

s = input('Enter Any String: ')
r = reversed(s)
print(type(r))  # <class 'reversed'>
print(r)

s = input('Enter Any String: ')
r = reversed(s)
output = ''.join(r)
print(output)

s = input('Enter Any String: ')
r = reversed(s)
output = '-'.join(r)
print(output)

s = input('Enter Any String: ')
r = reversed(s)
output = ''.join(r)
print(type(output))
print(output)

s = input('Enter Any String: ')
i = len(s) - 1
target = ''
while i >= 0:
    target = target + s[i]
    i = i - 1
print(target)

# Write a program to print characters at odd position and even position for the given string?
# s='abcdefgh'
# characters present at even position: a,c,e,g
# characters present at odd position: b,d,f,h

s = input('Enter any string: ')
print('Characters at Even position:', s[::2])
print('Characters at odd position:', s[1::2])

s = input('Enter any string: ')
print('Characters at Even position:')
i = 0
while i < len(s):
    print(s[i], end=' ')
    i = i + 2
print()
print('Characters at odd position:')
i = 1
while i < len(s):
    print(s[i], end=' ')
    i = i + 2

s = input('Enter any string: ')
evens = []
odds = []
i = 0
while i < len(s):
    if i % 2 == 0:
        evens.append(s[i])
    else:
        odds.append(s[i])
    i = i + 1
print(evens)
print(odds)

s = 'B4A1D3'
s1 = s2 = ''
for x in s:
    if x.isalpha():
        s1 = s1 + x
    else:
        s2 = s2 + x
print(s1)  # BAD
print(s2)  # 413

s = input('Enter any alphanumeric string: ')
s1 = s2 = ''
for x in s:
    if x.isalpha():
        s1 = s1 + x
    else:
        s2 = s2 + x
output = ''
for x in sorted(s1):
    output = output + x
for x in sorted(s2):
    output = output + x
print(output)

s = input('Enter any alphanumeric string: ')
s1 = s2 = ''
for x in s:
    if x.isalpha():
        s1 = s1 + x
    else:
        s2 = s2 + x
output = ''.join(sorted(s1) + sorted(s2))
print(output)

s = 'a4b3c2'
output = ''
for x in s:
    if x.isalpha():
        ch = x
    else:
        output = output + ch * int(x)
print(output)

s = 'AAAABBBBBBBBBBCCCCCCCCCCDDDDDDDDDDAAAAAEEEEEEE'
l = []
for x in s:
    if x not in l:
        l.append(x)
output = ''.join(l)
print(output)

s = input('Enter Any String: ')
l = []
for x in s:
    if x not in l:
        l.append(x)
output = ' '.join(sorted(l))
output = output.replace(' ', '')
print(output)






-------------
# Q1. Write a program to display the given number of *'s in a single row???

n = int(input('Enter n Value: '))
for i in range(n):
    print('*', end=' ')
    
    
# Q2. Write a program to print *'s in square pattern???
# n=3

n = int(input('Enter n Value: '))
for i in range(n):  # for every row
    for j in range(n):  # in every row or columns
        print('*', end=' ')
    print()

n = int(input('Enter n Value: '))
for i in range(n):  # for every row
    symbol = str(n) + ' *'
    print(symbol * n)

n = int(input('Enter n Value: '))
for i in range(n):  # for every row, i=0,1,2,3,...,n-1
    print((str(i + 1) + ' ') * n)  # n=3

n = int(input('Enter n Value: '))
for i in range(n):  # for every row
    for j in range(n):  # for every column in that row
        print(i + 1, end=' ')
    print()

n = int(input('Enter n Value: '))
for i in range(n):  # for every row, i=0,1,2,3,4,...,n-1
    for j in range(n):  # j=0,1,2,3,4,...n-1
        print(j + 1, end=" ")
    print()

n = int(input('Enter n Value: '))
for i in range(1, n + 1):  # for every row, i=1,2,3,4,...,n
    for j in range(1, n + 1):  # j=1,2,3,4,...n
        print(j, end=' ')
    print()

n = int(input('Enter n Value: '))
for i in range(n):  # for every row, i=0,1,2,3,4,...,n-1
    for j in range(n):  # j=0,1,2,3,4,...n-1
        print(n - j, end=' ')
    print()

