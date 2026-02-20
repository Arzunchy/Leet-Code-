class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]: #comparing to skip duplicate
                nums[k] = nums[i] # place unique
                k += 1
        return k  #time complexity O(n)amd S O(1)

