class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReqs = {c:[] for c in range(numCourses)}
        for crs, preq in prerequisites:
            preReqs[crs].append(preq)

        output = []
        visited, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True

            cycle.add(crs)

            for pre in preReqs[crs]:
                if dfs(pre) == False:
                    return False
            
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return output