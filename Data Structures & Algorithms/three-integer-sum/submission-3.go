import "slices"

func threeSum(nums []int) [][]int {
    res := make([][]int, 0)

    // Sort the input array
    slices.Sort(nums)

    // Iterate until you get to a positive num (no pairs after positive)
    // Move the pointer forward if it is the same as the previous number
    // Create a new l and r pointer, move them inward until you find a match
    for i := range nums {
        a := nums[i]
        if a > 0 {
            break
        }
        if i > 0 && a == nums[i - 1] {
            continue
        }

        l := i + 1
        r := len(nums) - 1

        for l < r {
            sum := a + nums[l] + nums[r]
            if sum == 0 {
                res = append(res, []int{a, nums[l], nums[r]})
                l++
                r--
                for l < r && nums[l] == nums[l - 1] {
                    l++
                }
            } else if sum > 0 {
                r--
            } else {
                l++
            }
        }
    }

    return res
}
