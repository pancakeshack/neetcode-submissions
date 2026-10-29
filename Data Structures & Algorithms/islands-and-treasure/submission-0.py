class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        seen = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    seen.add((r, c))

        def addCell(r, c):
            if (
                r not in range(ROWS)
                or c not in range(COLS)
                or (r, c) in seen
                or grid[r][c] == -1 
            ):
                return
            q.append([r, c])
            seen.add((r, c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                
                grid[r][c] = dist

                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1