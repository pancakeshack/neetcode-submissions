class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negs = [-n for n in nums]
        heapq.heapify(negs)

        res = 0

        while k > 0:
            res = -heapq.heappop(negs)
            k -= 1

        return res