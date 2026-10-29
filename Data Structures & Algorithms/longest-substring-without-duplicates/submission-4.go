func lengthOfLongestSubstring(s string) int {
    res := 0

    // Create l and r pointers
    // Grow the window until we see a repeating character
    // Keep a map a char:index so we can track what we have seen
    // Shrink the window the seen[char] when we see a character
    seen := make(map[byte]int)
    l := 0
    for r := 0; r < len(s); r++ {
        if i, exists := seen[s[r]]; exists {
            for l < i + 1 {
                delete(seen, s[l])
                l++
            }
        }
        seen[s[r]] = r
        res = max(res, r - l + 1)
    }

    return res
}
