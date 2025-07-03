# Question: Write a Python program to print the Fibonacci series up to n terms using recursion.


# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

# n = 7
# print([fibonacci(i) for i in range(n)])  
# Output: [0, 1, 1, 2, 3, 5, 8]



def fibo (n):
    if n <= 1:
        return n 
    return fibo(n-1) + fibo(n-2)

n=8
print ([fibo(i) for i in range(n)])