class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l, r = 0, 0
        length = len(s)

        seen = set()

        while r < length:
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            ans = max(ans, r - l + 1)
            r += 1

        return ans



        