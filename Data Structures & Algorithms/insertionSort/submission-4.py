# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)

        if n <= 1:
            if n == 0:
                return []
            else:
                return [pairs]

        ans = [pairs[:]]

        for i in range(1, n):
            j = i

            while j > 0 and pairs[j - 1].key > pairs[j].key:
                 pairs[j], pairs[j - 1] = pairs[j - 1], pairs[j]
                 j -= 1
            
            ans.append(pairs[:])
        
        return ans

