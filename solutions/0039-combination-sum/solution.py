class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def bt(i,s,sub):
            if s == target:
                res.append(sub.copy())
                return

            for j in range(i,len(candidates)):
                if s + candidates[j]<=target:
                    sub.append(candidates[j])
                    bt(j,s+candidates[j],sub)
                    sub.pop()

        bt(0,0,[])
        return res
