s = "hello"
if len(s)>1:
    l = list(s)
    l[0], l[-1] = l[-1],l[0]
    t = "".join(l)
print(t)