class Solution:
    def rob(self, nums: List[int]) -> int:
        def calc(houses):
            rob1, rob2 = 0, 0

            for n in houses:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp

            return rob2

        return max(nums[0], calc(nums[1:]), calc(nums[:-1]))