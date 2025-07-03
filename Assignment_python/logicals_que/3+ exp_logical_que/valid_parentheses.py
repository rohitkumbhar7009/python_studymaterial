# Question: Check if a given string of parentheses is valid.


def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    
    return not stack

print(is_valid("()[]{}"))  # Output: True
print(is_valid("(]"))      # Output: False
