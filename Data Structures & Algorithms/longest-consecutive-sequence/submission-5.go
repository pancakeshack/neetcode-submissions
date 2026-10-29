func longestConsecutive(nums []int) int {
    set := make(map[int]struct{}, len(nums))
    for _, num := range nums {
        set[num] = struct{}{}
    }

    seq := 0
    
    for _, num := range nums {
        if _, ok := set[num - 1]; !ok {
            length := 1
            for {
                _, next := set[num + length]
                if !next {
                    break
                }
                length++
            }
            seq = max(seq, length)
        }
    } 

    return seq
}
