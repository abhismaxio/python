s="a hi my hello world"
subString ="hello"
r = len(subString)
for i in range(len(s)-r+1):
    if s[i:i+r]==subString:
        print("yes")
        break
print("NO")
