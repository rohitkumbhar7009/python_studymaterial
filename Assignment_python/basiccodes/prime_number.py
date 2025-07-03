# Check if a number is prime

num = int(input("Enter a Number :  "))
is_prime = True

for i in range (2,num):
 if num % i == 0:
   is_prime = False
    
print ("prime " if is_prime else "Not prime")