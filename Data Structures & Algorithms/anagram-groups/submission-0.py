class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for i in range(len(strs)):
            temp = ''.join(sorted(strs[i]))

            if temp in groups:
                groups[temp].append(strs[i])
            else:
                groups[temp] = [strs[i]]

        ans = []
        for value in groups.values():
            ans.append(value)

        return ans
        