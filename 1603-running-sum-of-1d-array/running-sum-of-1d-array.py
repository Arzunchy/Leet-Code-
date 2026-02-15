class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=[]
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            n.append(total)
        return n
        
        