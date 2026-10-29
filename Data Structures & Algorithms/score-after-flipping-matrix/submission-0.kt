class Solution {
    fun matrixScore(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        var res = 0

        for (c in 0..<n) {
            var ones = 0
            for (row in grid) {
                if (row[c] == row[0]) ones++
            }
            res += maxOf(ones, m - ones) * (1 shl (n - 1 - c))
        }

        return res
    }
}