def remove_adjacent (s):
    stack=[]
    for char in s:
        print(char)
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
            print(stack)
    print (stack)
    return "".join(stack)

print(remove_adjacent("abbadfa"))