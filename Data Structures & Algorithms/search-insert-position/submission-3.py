class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #bruteforce
        for i in range(len(nums)):
            if nums[i]>=target:
                return i
        return len(nums)
        

        

