# Fibonacci sequence up to n terms


n = int(input("Enter the number of terms: "))

# First two Fibonacci numbers
a = 0
b = 1

# Print the Fibonacci sequence
for _ in range(n):
    print(a)
    # Update a and b to the next numbers
    c = a + b
    a = b
    b = c  
     

