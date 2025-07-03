# number = 2
# print(number > 3)
# print(number < 3)
# print(not number > 3)
# print(not number < 3)
# print(number > 3 and number > 1)
# print(number > 3 or number > 1)



# Result =>
# False
# True
# True
# False
# False
# True


# ------------------------------------------------------------------------------------------------------------------

# first = input("Enter first number : ")
# second = input("Enter second number : ")
# first = int(first)
# second = int(second)
# print("----press keys for operator (+,-,*,/,%)----------")
# operator = input("Enter operator : ")
# operator == "+"
# print (first + second)
# operator == "-"
# print(first - second)
# elif operator == "*":
# print(first * second)
# elif operator == "/":
# print(first / second)
# elif operator == "%":
# print(first % second)
# else:
# print("Invalid Operation")



# ------------------------------------------------------------------------------------------------------------------




# i = 1
# while(i <= 5):print(i)
# i = i + 1
# i = 1
# while(i <= 5):print(i * "*")
# i = i + 1
# i = 5
# while(i >= 1): print(i * "*")
# i = i - 1

# /////////////////////////////////////////////////////////////////////////////
# for i in range(5):
#     print(i)
# i = i + 1
# for i in range(5): print(i * "*")
# i = i + 1


# result=>
# 0
# 1
# 2
# 3
# 4

# *
# **
# ***
# ****

# ------------------------------------------------------------------------------------------------------------------


# friends = ["amar", "akbar", "anthony"]
# print(friends[0])
# print(friends[1])
# print(friends[-1])
# print(friends[-2])
# friends[0] = "aman"
# print(friends)
# print(friends[0:2]) #returns a new list
# for friend in friends:print(friend)


# result=>
# amar
# akbar
# anthony
# akbar
# ['aman', 'akbar', 'anthony']
# ['aman', 'akbar']
# aman
# akbar
# anthony

# ------------------------------------------------------------------------------------------------------------------

# marks = ["english", 95, "chemistry", 98]
# marks.append("physics")
# marks.append(97)
# print(marks)
# marks.insert(0, "math")
# marks.insert(1, 99)
# print(marks)
# print("math" in marks)
# print(len(marks)/2)
# marks.clear()
# print(marks)

# not solve
# i = 0
# while i < len(marks):print(marks[i])
# print(marks[i+1])
# i = i + 2

# result =>
# ['english', 95, 'chemistry', 98, 'physics', 97]
# ['math', 99, 'english', 95, 'chemistry', 98, 'physics', 97]
# True
# 4.0
# []


# ------------------------------------------------------------------------------------------------------------------

# students = ["ram", "shyam", "kishan", "radha", "radhika"]
# for student in students:
#     if(student == "radha"):break 
# print(student)
# for student in students: 
#     if(student == "kishan"):continue
# print(student)

# result=>
# radha
# radhika


# ------------------------------------------------------------------------------------------------------------------


# tuple 


# marks = (95, 98, 97, 97)
# marks[0] = 98
# print(marks.count(97))
# print(marks.index(97))


# result=> 
# 2
# 2


# ------------------------------------------------------------------------------------------------------------------

# set 
# marks = {98, 97, 95, 95}
# print(marks)
# for score in marks:print(score)


# result=>
# {97, 98, 95}
# 97
# 98
# 95

# ------------------------------------------------------------------------------------------------------------------

# Dictionary
# marks = {"math" : 99, "chemistry" : 98, "physics" : 97}
# print(marks)
# print(marks["chemistry"])
# marks["english"] = 95
# print(marks)
# marks["math"] = 96
# print(marks)


# result=>
# {'math': 99, 'chemistry': 98, 'physics': 97}
# 98
# {'math': 99, 'chemistry': 98, 'physics': 97, 'english': 95}
# {'math': 96, 'chemistry': 98, 'physics': 97, 'english': 95}


# ------------------------------------------------------------------------------------------------------------------



# Module Function 
# import math
# print(dir(math))
# import random
# print(dir(random))
# import string
# print(dir(string))
# from math import sqrt
# print(sqrt(4))


# ------------------------------------------------------------------------------------------------------------------

#  User-dened functions           
# def sum(a, b=4):
#     print(a + b)
# sum(1, 2)
# sum(1)

# result=>
# 3
# 5

