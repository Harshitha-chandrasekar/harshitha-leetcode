class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s) # no of characters in s
        l = 0 # length of longest string
        for i in range(0,n):
            x = 0
            arr = []
            for j in range(i,n):
                ch = s[j]
                if ch not in arr:
                    arr = arr + [ch]
                    x = x + 1
                else:
                    break

            if x > l:
                l = x
                x = 0

        return  l

        
