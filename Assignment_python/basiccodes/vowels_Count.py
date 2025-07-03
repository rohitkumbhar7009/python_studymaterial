# Count vowels in a string


s =  str(input(" Enter a name :  "))
count = 0 
for char in s :
    if char in "aeiouAEIOU" :
        count += 1
print(count)
