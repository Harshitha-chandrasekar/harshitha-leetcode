class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def bt(i,scentence,res):
            if i == len(s):
                res.append(" ".join(scentence))
                return

            for j in range(i,len(s)):
                word = s[i:j+1]
                if word in wordDict:
                    scentence.append(word)
                    bt(j+1,scentence,res)
                    scentence.pop()


        res = []
        bt(0,[],res)
        return res
