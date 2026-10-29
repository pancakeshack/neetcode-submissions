class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [0] * n

        for i in range(m - 1, -1, -1):
            nextRow = [0] * n
            nextRow[n - 1] = 1
            for j in range(n - 2, -1, -1):
                nextRow[j] = nextRow[j + 1] + prevRow[j]
            prevRow = nextRow
        
        return prevRow[0]