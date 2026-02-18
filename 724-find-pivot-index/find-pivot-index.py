class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        left = sum(nums)
        for i in range(len(nums)):
            if total == left - nums[i]:# checks left sum is eqaul to right sum if return i
                return i
            total += nums[i]
            left -= nums[i]
        return -1


