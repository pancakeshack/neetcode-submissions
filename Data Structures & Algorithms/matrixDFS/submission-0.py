class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def helper(grid, r: int, c: int, visit: set) -> int:
            if (r == ROWS or c == COLS
            or min(r, c) < 0 or (r, c) in visit
            or grid[r][c] == 1):
                return 0
            
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            visit.add((r, c))

            res = 0

            res += helper(grid, r + 1, c, visit)
            res += helper(grid, r - 1, c, visit)
            res += helper(grid, r, c + 1, visit)
            res += helper(grid, r, c - 1, visit)

            visit.remove((r, c))
            return res

        
        return helper(grid, 0, 0, set())