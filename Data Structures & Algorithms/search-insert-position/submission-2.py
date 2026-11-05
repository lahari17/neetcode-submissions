class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #bruteforce
        if target<nums[0]:
            return 0
        elif target>nums[len(nums)-1]:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i]< target and nums[i+1]> target:
                return i+1
        

        

