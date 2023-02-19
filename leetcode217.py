class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # solve using loop
        for i in nums:
            if nums.count(i) > 1:
                return True
        # solve using length
        return (len(nums) != len(set(nums)))
        
