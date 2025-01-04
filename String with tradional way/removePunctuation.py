s = "hello, world"
punctuation = ".,!?;:"
result = ""
for char in s:
    if char not in punctuation:
        result+=char
print(result)