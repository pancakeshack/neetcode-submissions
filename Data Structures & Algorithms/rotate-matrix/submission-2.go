func rotate(matrix [][]int)  {
    left := 0
    right := len(matrix) - 1

    for left < right {
        for i := range right - left {
            top := left
            bottom := right

            tmpTL := matrix[top][left + i]

            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = tmpTL
        }
        left++
        right--
    }
}
