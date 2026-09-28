class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        i = 1 
        s = [1]
        ans = []
        ans.append([i])
        while i<numRows:
            news = [s[0]]
            for j in range(len(s)-1):
                news.append(s[j]+s[j+1])
            news.append(s[-1])
            ans.append(news)
            s = news
            i+= 1
            
        return ans
