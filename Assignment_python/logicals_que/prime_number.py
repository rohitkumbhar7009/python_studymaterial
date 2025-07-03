






# Question: Write a function to check if a number is prime or not.

# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# print(is_prime(29))  # Output: True
# print(is_prime(10))  # Output: False


def is_okPrime(num):
    if num <=1:
        return False
    for i in range(2,int(num ** 0.5) +1 ):
        if num % i == 0:
            return False
    return True
print (is_okPrime(9))
    
