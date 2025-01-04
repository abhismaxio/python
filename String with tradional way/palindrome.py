s = "madasdam"
l = len(s)
is_palindrome =True
for i in range(l//2):
    if s[i] != s[len(s)-i-1]:
        is_palindrome = False
        break
print(is_palindrome)