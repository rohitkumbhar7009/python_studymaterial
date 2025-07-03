# Question: Write a Python program to count vowels and consonants in a string.

def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v_count = sum(1 for ch in s if ch in vowels)
    c_count = sum(1 for ch in s if ch.isalpha() and ch not in vowels)
    return v_count, c_count

print(count_vowels_consonants("hello world"))  # Output: (3, 7)
