from collections import Counter

def min_window(s, t):
        if not s or t:
            return ""
        window = {}
        t_count = Counter(t)
        have , need = 0, len(t_count)
        res , res_len = [-1,-1], float("inf")
        left = 0
        print 
        print(len(s))
        for right in range(12):
            char = s[right]
            print(right)
            window[char] = window.get(char,0)+1
            if char in t_count and window[char] == t_count[char]:
                have+=1
            while have == need:
                if right -left +1 < res_len:
                    res = [left,right]
                    res_len= right -left+1
                window[s[left]] -=1
                if s[left] in t_count and window[s[left]]<t_count[s[left]]:
                    have-=1
                left+=1
        left,right =res
        return s[left:right + 1] if res_len != float("inf") else ""





print(min_window("ADAOBECODEBANC", "ABC"))
