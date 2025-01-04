s = "hello"
upper = ""
for char in s:
    if 'a' <= char <= 'z':
        upper += chr(ord(char) - ord('a') + ord('A'))
    else:
        upper += char
print(upper)

lower=""
for char in s:
    if 'A'<= char <= "Z":
        lower+= chr(ord(char)- ord('A')+ord('a'))
    else:
        lower+= char
print(lower)