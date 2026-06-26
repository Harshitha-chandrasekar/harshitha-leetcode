class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        news = ""
        i,j = 0,0
        while  i<len(word1) and j<len(word2):
            news = news + word1[i] + word2[j]
            i = i+1
            j = j+1
        while i<len(word1):
            news = news + word1[i]
            i = i+1
        while j<len(word2):
            news = news + word2[j]
            j = j+1
        return news
