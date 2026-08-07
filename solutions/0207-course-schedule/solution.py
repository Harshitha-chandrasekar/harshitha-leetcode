class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dictpre = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            dictpre[crs].append(pre)
        checked = set()
        
        def dfs(crs):
            if crs in checked:
                return False

            if dictpre[crs] == []:
                return True

            checked.add(crs)

            for req in dictpre[crs]:
                if not  dfs(req):
                    return False


            checked.remove(crs)

            dictpre[crs] = []

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
