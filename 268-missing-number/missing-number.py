class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for _ in range(len(nums)+1):
            if _ not in nums:
                return _