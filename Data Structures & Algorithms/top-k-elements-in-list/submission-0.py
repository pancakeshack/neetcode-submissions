class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        ans = []

        for i in range(k):
            max_key = max(counts, key=counts.get)
            del counts[max_key]
            ans.append(max_key)

        return ans