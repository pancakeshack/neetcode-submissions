class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}

        for i in range(len(nums)):
            needed = target - nums[i]
            
            if needed in sums:
                return sorted([i, sums[needed]])
            else:
                sums[nums[i]] = i