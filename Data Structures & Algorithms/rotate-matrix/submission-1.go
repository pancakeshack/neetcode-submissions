func rotate(matrix [][]int)  {
    left := 0
    right := len(matrix) - 1

    for left < right {
        for i := range right - left {
            top := left
            bottom := right

            tmpTL := matrix[top][left + i]
            tmpTR := matrix[top + i][right]
            tmpBR := matrix[bottom][right - i]
            tmpBL := matrix[bottom - i][left]

            matrix[top + i][right] = tmpTL
            matrix[bottom][right - i] = tmpTR
            matrix[bottom - i][left] = tmpBR
            matrix[top][left + i] = tmpBL
        }
        left++
        right--
    }
}
