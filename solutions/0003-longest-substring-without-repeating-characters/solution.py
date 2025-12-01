class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        left = 0
        max_length = 0
        hash = {}
        
        for right in range(n):
            ch = s[right] # current letter
            if ch in hash and hash[ch] >= left:
                left = hash[ch] +1
            hash[ch] = right

            max_length = max(max_length, right- left +1)

        return max_length
        
        
