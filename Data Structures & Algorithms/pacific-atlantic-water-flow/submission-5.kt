typealias Point = Pair<Int, Int>

class Solution {
    val directions = arrayOf(intArrayOf(0, 1), intArrayOf(0, -1), intArrayOf(-1, 0), intArrayOf(1, 0))

    fun pacificAtlantic(heights: Array<IntArray>): List<List<Int>> {
        val rows = heights.size
        val cols = heights[0].size

        val atlantic = HashSet<Point>()
        val pacific = HashSet<Point>()

        fun dfs(r: Int, c: Int, set: HashSet<Point>) {
            set.add(r to c)
            for (dir in directions) {
                val nr = dir[0] + r
                val nc = dir[1] + c
                if (nr in 0..<rows && nc in 0..<cols && !set.contains(nr to nc)
                    && heights[nr][nc] >= heights[r][c]) {
                    dfs(nr, nc, set)
                }
            }
        }

        for (r in 0 until rows) {
            dfs(r, 0, pacific)
            dfs(r, cols - 1, atlantic)
        }
        for (c in 0 until cols) {
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)
        }

        val result = mutableListOf<List<Int>>()
        for (point in pacific) {
            if (atlantic.contains(point)) {
                result.add(listOf(point.first, point.second))
            }
        }
        
        return result
    }
}