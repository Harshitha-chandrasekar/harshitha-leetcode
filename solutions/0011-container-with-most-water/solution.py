class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        curr_m = 0
        i = 0
        j = len(height)-1
        while(i<j):
            curr_m = max(curr_m,(j-i)*min(height[i],height[j]))
            if height[i] < height[j]:
                i = i+1
            else:
                j = j-1

        return curr_m
        
