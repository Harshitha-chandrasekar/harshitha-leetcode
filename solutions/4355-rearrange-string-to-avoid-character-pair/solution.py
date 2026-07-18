class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        ans = ""
        count_of_x = 0
        for c in s:
            if c!=x:
                ans = ans + c
            else:
                count_of_x+=1

        ans = ans + count_of_x*x
        return ans
            
