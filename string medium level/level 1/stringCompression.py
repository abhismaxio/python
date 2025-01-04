def compress(s):
    if not s:
        return ""
    result =[]
    count =1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            count +=1
        else:
            result.append(s[i-1])
            if count>1:
                for digit in str(count):
                    result.append(digit)
            count =1
    result.append(s[-1])
    result.append(str(count))
    return result

print(compress("pppppppppppppppppppppppasaaaasssss"))
