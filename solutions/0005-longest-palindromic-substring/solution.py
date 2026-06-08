class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[False]*n for _ in range(n)]

        start = 0
        max_len = 1
        for i in range(n):
            dp[i][i] = True

        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if s[i] == s[j]:
                    if j-i<2 or dp[i+1][j-1]:
                        dp[i][j] = True


                        curr = j-i+1
                        if curr>max_len:
                            max_len = curr
                            start = i

        return s[start:start+max_len]  
        
