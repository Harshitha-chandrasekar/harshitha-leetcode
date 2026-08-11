class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if '0000' in visited:
            return -1

        def children(num):
            res = []
            for i in range(4):
                digit = str((int(num[i])+1)%10)
                res.append(num[:i]+digit+num[i+1:])
                digit = str((int(num[i])-1+10)%10)
                res.append(num[:i]+digit+num[i+1:])
            return res

        q = deque([('0000',0)])
        while q:
            num,turns = q.popleft()
            if num == target:
                return turns

            for child in children(num):
                if child not in visited:
                    visited.add(child)
                    q.append((child,turns+1))

        return -1
