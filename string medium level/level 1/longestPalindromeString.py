def palindromeString(s):
    def expandFromCenter(left,right):
        while left>=0 and right<len(s) and s[left]==s[right] :
            left -= 1
            right += 1
        return s[left+1:right]
    longest=''
    for i in range(len(s)):
        odd =expandFromCenter(i,i)
        even= expandFromCenter(i,i+1)
        longest = max(odd,even,longest,key=len)
    return longest
print(palindromeString("bcabd"))