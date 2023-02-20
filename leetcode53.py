class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currentMax = nums[0]
        total = 0
        for i in range(len(nums)):
            if total < 0:
                total = 0
            total += nums[i]
            currentMax = max(currentMax,total)
        return currentMax
