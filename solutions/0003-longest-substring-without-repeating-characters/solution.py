class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        elements = {}
        currmax = 0
        left = 0
        for right in range(len(s)):
            currentch = s[right]

            if currentch in elements and elements[currentch] >= left:
                left = elements[currentch]+1

            elements[currentch] = right

            currmax = max(currmax,right-left+1)

        return currmax



