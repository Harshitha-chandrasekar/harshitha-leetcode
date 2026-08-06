class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m,n = len(s),len(t)
        count = {}
        for c in t:#O(n)
            if c in count:
                count[c]+=1
            else:
                count[c]=1
        minss = ""
        minlen = float('inf')
        l = 0
        tofind = n
        for r in range(m):
            if s[r] in count:
                if count[s[r]]>0:
                    tofind-=1
                count[s[r]] -= 1
            while tofind == 0:
                if (r-l+1) < minlen:
                    minlen = r-l+1
                    minss = s[l:r+1]
                if s[l] in count:
                    count[s[l]] += 1
                    if count[s[l]] > 0:
                        tofind += 1
                l+=1

        return minss

        
