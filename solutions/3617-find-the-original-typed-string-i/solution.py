class Solution(object):
    def possibleStringCount(self, word):
        count = 0
        length = len(word)
        for i in range(0,length-1):
            if word[i] == word[i+1]:
                count = count + 1

        count = count + 1
        return count

        
