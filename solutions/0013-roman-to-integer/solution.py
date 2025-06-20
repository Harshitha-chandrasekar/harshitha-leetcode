class Solution(object):
    def romanToInt(self, s):
        l = len(s)
        numeric = 0
        roman_val ={'I':1,'V':5,"X":10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(0,l-1):
            if roman_val[s[i]] < roman_val[s[i+1]]:
                numeric = numeric - roman_val[s[i]]
            else:
                numeric = numeric + roman_val[s[i]]
        numeric = numeric + roman_val[s[l-1]]
        return numeric
                
        
