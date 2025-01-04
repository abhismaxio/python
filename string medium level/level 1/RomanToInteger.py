def roman_to_int(s):
    roman = {'I':1,'V':5,'X':10,'L':50,'c':100,'D':500,'M':1000}
    total =0
    prev=0
    for char in reversed(s):
        current = roman[char]
        if current >=prev:
            total += current
        else:
            total -= current
        prev = current
    return total
    


print(roman_to_int("LIVII"))