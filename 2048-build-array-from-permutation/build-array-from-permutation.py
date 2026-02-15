class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for _ in range(len(nums)): # loop start from 0 to n-1;
            ans.append(nums[nums[_]]) #we add value inside the ans=[nums]
        return ans



