class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums1={}
        for i in range(len(nums)):
            if target-nums[i] in nums1:
                return [nums1[target-nums[i]],i]
            else:
                nums1[nums[i]]=i

    
