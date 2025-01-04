s = "hello World"
old ="hell"
new="ven"
result =""
i=0
for i in range(len(s)-len(old)+1):
    if s[i:i+len(old)]==old:
        result += new
        i+= len(new)
    else:
        result += s[i]
        i+=1
print(result)