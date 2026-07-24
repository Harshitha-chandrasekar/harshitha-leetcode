class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def bt(i):
            if i>=len(s):
                res.append(part.copy())
                return

            for j in range(i,len(s)):
                temp = s[i:j+1]
                if temp == temp[::-1]:
                    part.append(s[i:j+1])
                    bt(j+1)
                    part.pop()

        bt(0)
        return res
