class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        maxl = max(len(word) for word in words)
        output = [""] * maxl
        for word in words:
            for i in range(maxl):
                if i<len(word):
                    output[i] += word[i]
                else:
                    output[i] += " "

        ans = []
        for word in output:
            while word[-1] == " ":
                word = word[:-1]
            ans.append(word)

        return ans
