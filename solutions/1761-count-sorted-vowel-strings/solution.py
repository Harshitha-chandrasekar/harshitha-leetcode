class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24
