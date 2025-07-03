# Question: Write a Python program to find the second largest number in an array.

def second_largest(arr):
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second

print(second_largest([10, 20, 4, 45, 99]))  # Output: 45
