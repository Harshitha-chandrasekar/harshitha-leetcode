class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        maxl = 1
        start = 0
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if s[i] == s[j]:
                    if j-i<2 or dp[i+1][j-1]:
                        dp[i][j] = True

                        if j-i+1>maxl:
                            maxl = j-i+1
                            start = i
        
        return s[start:start+maxl]

