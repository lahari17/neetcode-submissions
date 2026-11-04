class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sub_sum=0
        min_length = float("inf")
        
        for right in range(len(nums)):
            sub_sum= sub_sum + nums[right]
            while sub_sum>=target:
                min_length = min(min_length, right-left+1)
                sub_sum= sub_sum - nums[left]
                left = left +1
                
        return 0 if min_length == float("inf") else min_length
            

