class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Counts = defaultdict(int)

        for c in range(len(s1)):
            s1Counts[s1[c]] += 1

        s2Counts = defaultdict(int)
        l = 0

        for r in range(len(s2)):
            s2Counts[s2[r]] += 1
            
            while (r - l + 1) > len(s1):
                s2Counts[s2[l]] -= 1

                if s2Counts[s2[l]] == 0:
                    del s2Counts[s2[l]]

                l += 1

            if s2Counts == s1Counts:
                return True
        
        return False