class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dicti = defaultdict(list)
        for x,y in prerequisites:
            dicti[x].append(y)

        ans = []

        for start,target in queries:
            q = deque([start])
            seen = set()
            visit = set()
            while q:
                node = q.popleft()
                for req in dicti[node]:
                    if req not in seen:
                        seen.add(req)
                        q.append(req)
                    visit.add(req)
            if target in visit:
                ans.append(True)
            else:
                ans.append(False)

        return ans
            
