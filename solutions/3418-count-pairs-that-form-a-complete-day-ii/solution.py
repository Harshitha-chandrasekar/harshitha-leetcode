class Solution(object):
    def countCompleteDayPairs(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        freq = {}
        ans = 0
        for i in hours:
            r = i%24
            need = (24-r)%24
            ans = ans + freq.get(need,0)
            freq[r] = freq.get(r,0)+1
        return ans
