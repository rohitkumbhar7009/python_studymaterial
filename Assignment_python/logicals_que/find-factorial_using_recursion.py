# Question: Write a recursive Python function to find the factorial of a number.

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n-1)

# print(factorial(5))  # Output: 120  (1*2*3*4*5)


def fact(s):
    if s == 0 or s == 1:
        return 1
    return s * fact (s -1)
print(fact(4) )
