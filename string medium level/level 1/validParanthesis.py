def is_valid_parentheses(s):
    stack=[]
    mapping = {")":"(","}":"{","]":"[" }
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            print(char)
            stack.append(char)
    print("stack is ",stack)
    return not stack


# Example
   # Output: False
print(is_valid_parentheses("{[{}}]}"))    # Output: True