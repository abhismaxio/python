from typing import List
def compress(chars):
    result =0
    i=0
    while i< len(chars):
        letter = chars[i]
        count =0
        while i<len(chars) and chars[i]==letter:
            count +=1
            i+=1
        chars[result]=letter
        result+=1
        if count > 1:
            for c in str(count):
                chars[result]=c
                result+=1
    while len(chars)>result:
        chars.pop()


chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]

compress(chars) # Output: 4
print(chars)