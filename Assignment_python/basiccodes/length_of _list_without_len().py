#  Length of a list without using len()  input used 

r = input("Enter list element : ").split()

count = 0

for _ in r :
    count += 1
print(count)