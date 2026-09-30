class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        i = 1 
        s = [1]
        while i<=rowIndex:
            news = [s[0]]
            for j in range(len(s)-1):
                news.append(s[j]+s[j+1])
            news.append(s[-1])
            s = news
            i+= 1
            
        return s
