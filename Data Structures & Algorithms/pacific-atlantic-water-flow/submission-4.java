class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        final int rows = heights.length;
        final int cols = heights[0].length;
        List<List<Integer>> result = new ArrayList<>();
        Set<List<Integer>> pacific = new HashSet<>();
        Set<List<Integer>> atlantic = new HashSet<>();

        for (int i = 0; i < cols; i++) {
            dfs(heights, pacific, 0, i, 0);
            dfs(heights, atlantic, rows - 1, i, 0);
        }
        for (int i = 0; i < rows; i++) {
            dfs(heights, pacific, i, 0, 0);
            dfs(heights, atlantic, i, cols - 1, 0);
        }

        for (var p : pacific) {
            if (atlantic.contains(p)) {
                result.add(p);
            }
        }

        return result;
    }

    private void dfs(int[][] heights, Set<List<Integer>> set, int r, int c, int prev) {
        final int rows = heights.length;
        final int cols = heights[0].length;
        final List<Integer> pair = List.of(r, c);
        if (r >= rows || c >= cols || r < 0 || c < 0 || set.contains(pair) || heights[r][c] < prev) {
            return;
        }

        int cur = heights[r][c];
        set.add(pair);
        dfs(heights, set, r + 1, c, cur);
        dfs(heights, set, r - 1, c, cur);
        dfs(heights, set, r, c + 1, cur);
        dfs(heights, set, r, c - 1, cur);
    }
}
