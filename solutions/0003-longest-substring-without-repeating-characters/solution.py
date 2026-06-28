class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        maxl = 0
        l = 0
        r = 0
        while r<len(s):
            if s[r] not in sett:
                sett.add(s[r])
                r = r+1
                maxl = max(maxl,r-l)
            else:
                sett.remove(s[l])
                l = l+1
            if l>r:
                r = l+1

        return maxl

