# Question: Find the longest palindromic substring in a given string.



def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]

def longest_palindrome(s):
    longest = ""
    for i in range(len(s)):
        # Odd length palindrome
        odd = expand_around_center(s, i, i)
        # Even length palindrome
        even = expand_around_center(s, i, i + 1)
        longest = max(longest, odd, even, key=len)
    return longest

print(longest_palindrome("babad"))  # Output: "bab" or "aba"

