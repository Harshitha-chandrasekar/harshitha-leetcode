class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        cache = [-1]*n

        def dp(i):
            if i == n:
                return 1
            if i>n:
                return 0 
            if s[i] == '0':
                return 0
            if cache[i]!= -1:
                return cache[i]
            res = dp(i+1)

            if i+1<n and(s[i] == '1' or(s[i] == '2' and s[i+1] <= '6')):
                res = res + dp(i+2)

            cache[i] = res
            return res

        ans = dp(0)
        return ans
