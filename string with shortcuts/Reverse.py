s = input("enter a string: ")
s= list(s)
left, right = 0 , len(s)-1
while left < right:
    s[left], s[right] =s[right], s[left] 
    left = left + 1
    right = right - 1
print(s)