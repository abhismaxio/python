# "abcabcbb" → "abc" → Length: 3.
def longestSubstring(s):
    character_set = set()
    left=0
    max_length = 0
    for right in range(len(s) ):
        while s[right] in character_set:
            character_set.remove(s[right])
            left +=1
        character_set.add(s[right])
        max_length= max(max_length,right-left+1)
    return character_set,max_length

print(longestSubstring("abcabcbblksladnalsdnalskd"))