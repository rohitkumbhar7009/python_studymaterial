#  Find factorial using loop

# num =  3
# fact = 1 

# for  i in range (1, num + 1):
#     fact *= i
# print(fact)



nums = 6 
facts = 1 

for t in range(1,nums+1):
    facts *=t
    print(facts)


"""
 What is a Factorial?
The factorial of a number means:
Multiply that number by every smaller number down to 1.

Example:

5! (read as "5 factorial") = 5 × 4 × 3 × 2 × 1 = 120

3! = 3 × 2 × 1 = 6

1! = 1

0! = 1 (this is a special case and it's defined like this in math)
"""