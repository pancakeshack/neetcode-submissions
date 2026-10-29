func longestConsecutive(nums []int) int {
    set := make(map[int]struct{}, len(nums))
    for _, num := range nums {
        set[num] = struct{}{}
    }

    if len(nums) == 0 {
        return 0
    }
    seq := 1

    for _, num := range nums {
        if _, ok := set[num - 1]; !ok {
            cur := num + 1
            for {
                _, next := set[cur]
                if !next {
                    break
                }
                length := (cur - num) + 1
                seq = max(seq, length)
                cur++
            }
        }
    } 

    return seq
}
