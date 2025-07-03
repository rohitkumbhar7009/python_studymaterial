# Question: Given an array of numbers from 1 to n with one number missing, find the missing number.


def find_missing(arr):
    n = len(arr) + 1
    total_sum = n * (n + 1) // 2
    return total_sum - sum(arr)

print(find_missing([1, 2, 4, 5, 6]))  # Output: 3
