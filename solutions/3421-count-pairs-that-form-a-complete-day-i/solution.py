class Solution(object):
    def countCompleteDayPairs(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        count = 0
        hours.sort()
        for i in range(len(hours)):
            for j in range(i+1,len(hours)):
                if (hours[i] + hours[j]) % 24 == 0:
                    count = count +1

        return count
