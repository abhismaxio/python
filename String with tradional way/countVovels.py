s = input("Enter a number: ")
vowel ="aeiou"
count= 0
for char in s:
    if char in vowel:
        count += 1
print(count)


