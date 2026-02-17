class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        num=0
        maxSum=nums[0]
        for i in range(len(nums)):
            num+=nums[i]
            maxSum=max(num,maxSum)
            if num<0:
                num=0
        return maxSum