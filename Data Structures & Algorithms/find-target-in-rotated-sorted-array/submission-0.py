class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m

            if nums[m] > target:
                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m - 1

            elif nums[m] < target:
                if nums[m] > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1