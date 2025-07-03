# Question: Write a program to find duplicate elements in an array.

def find_duplicates(arr):
    duplicates = []
    seen = set()
    for num in arr:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)
    return duplicates

print(find_duplicates([1, 2, 3, 4, 2, 5, 6, 3]))  # Output: [2, 3]
