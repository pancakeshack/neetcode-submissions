func maxProfit(prices []int) int {
    res := 0

    // Iterate through prices using a left and right pointer
    // Update LEFT pointer when you encounter a new smallest element
    // Iterate until RIGHT reaches the end of the array
    // Update the result if price[r] - price[i] > res
    l := 0
    for r := 1; r < len(prices); r++ {
        if prices[r] < prices[l] {
            l = r
            continue
        }
        if prices[r] - prices[l] > res {
            res = prices[r] - prices[l]
        }
    }

    return res
}
