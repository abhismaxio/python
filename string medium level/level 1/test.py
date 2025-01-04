def compress( chars):
    if not chars:
        return ""
    result =[]
    count =1
    for i in range(1,len(chars)):
        if chars[i]==chars[i-1]:
            count+=1
        else:
            result.append(chars[i-1])
            for j in str(count):
                result.append(j)
            count =1
    result.append(chars[i-1])
    for j in str(count):
        result.append(j)
    return result

chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b","b", "b", "b", "b", "b", "b", "b", "b","b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
new_length = compress(chars)
print(new_length)  # Output: 4