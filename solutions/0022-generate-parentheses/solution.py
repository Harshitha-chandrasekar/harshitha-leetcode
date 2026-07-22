class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def bt(s,opened,closed):
            if opened == n and closed == n:
                res.append(s)
                return

            if opened<n and opened>=closed:
                bt(s+'(',opened+1,closed)

            if closed<n:
                bt(s+')',opened,closed+1)

        bt('',0,0)
        return res
