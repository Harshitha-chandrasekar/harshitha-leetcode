class Solution(object):
    def strStr(self, haystack, needle):
        if haystack == needle:
            return 0
        nlength = len(needle)
        for i in range(0,len(haystack)-nlength+1):
            if needle == haystack[i:i+nlength]:
                return i
        return -1
        
