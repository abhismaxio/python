  # Output: [0, 6]
from collections import Counter
def find_anagram(main,part):
    result=[]
    part_count=Counter(part)
    print(part_count)
    slide_w_count=Counter(main[:len(part)-1]) #side of one less than part
    print(slide_w_count)
    for i in range (len(part)-1,len(main)):
        print(i)
        slide_w_count[main[i]]+=1
        print(slide_w_count)
        if part_count==slide_w_count:
            result.append(i-len(part)+1)
            print("yes")
        slide_w_count[main[i-len(part)+1]]-=1
        if slide_w_count[main[i-len(part)+1]]==0:
            del slide_w_count[main[i-len(part)+1]]
    return result


print(find_anagram("cvbaebabacd", "eab")) 

