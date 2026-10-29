class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqs = {i:[] for i in range(numCourses)}
        for crs, preq in prerequisites:
            preReqs[crs].append(preq)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if preReqs[crs] == []:
                return True

            visited.add(crs)

            for preq in preReqs[crs]:
                if not dfs(preq):
                    return False
                
            visited.remove(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True