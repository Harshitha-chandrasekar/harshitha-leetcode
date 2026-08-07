class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        leftcandle = [-1] * n
        rightcandle = [-1] * n
        prefix_plates = [0] * n
        
        plates_so_far = 0
        last_candle = -1
        for i in range(n):
            if s[i] == '*':
                plates_so_far += 1
            elif s[i] == '|':
                last_candle = i
                
            prefix_plates[i] = plates_so_far
            leftcandle[i] = last_candle

        last_candle = -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                last_candle = i
            rightcandle[i] = last_candle

        ans = []
        for l, r in queries:
            left_bound = rightcandle[l]
            right_bound = leftcandle[r]
            
            if left_bound != -1 and right_bound != -1 and left_bound < right_bound:
                plates = prefix_plates[right_bound] - prefix_plates[left_bound]
                ans.append(plates)
            else:
                ans.append(0)
                
        return ans

