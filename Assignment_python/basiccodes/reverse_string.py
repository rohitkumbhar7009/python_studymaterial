#  Reverse a string


# ✅ 1. Using Slicing (most Pythonic)
s = "pritish"
print(s[::-1])


# ✅ 2. Using reversed() and join()
s = "pritish"
print(''.join(reversed(s)))


# ✅ 3. Using a for loop
s = "pritish"
rev = ''
for char in s:
    rev = char + rev
print(rev)


# ✅ 4. Using a while loop
s = "pritish"
i = len(s) - 1
rev = ''
while i >= 0:
    rev += s[i]
    i -= 1
print(rev)



# ✅ 5. Using recursion
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

s = "pritish"
print(reverse_string(s))


# ✅ 6. Using stack (list as LIFO)

s = "pritish"
stack = list(s)
rev = ''
while stack:
    rev += stack.pop()
print(rev)



# ✅ 7. Using reduce() from functools
from functools import reduce

s = "pritish"
rev = reduce(lambda x, y: y + x, s)
print(rev)
