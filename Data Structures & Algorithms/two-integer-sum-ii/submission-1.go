func twoSum(numbers []int, target int) []int {
    l := 0
    r := len(numbers) - 1

    res := make([]int, 2)
    // Iterate through nums with two pointers
    // If the total > target, r-- else l++
    // Loop until l >= r
    for l < r {
        sum := numbers[l] + numbers[r]
        switch {
        case sum == target:
            res[0] = l + 1
            res[1] = r + 1
            return res
        case sum > target:
            r--
        default:
            l++
        }
    }

    return res
}
