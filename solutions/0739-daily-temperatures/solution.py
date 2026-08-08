class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)

        for i in range(len(temperatures)):
            currtemp = temperatures[i]
            while stack and currtemp > stack[-1][0]:
                temp,idx = stack.pop()
                res[idx] = i-idx
            stack.append([currtemp,i])

        return res
        
