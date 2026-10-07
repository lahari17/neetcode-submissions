class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        longest = 1
        current_length=1
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            if nums[i]== nums[i-1]+1:
                current_length= current_length+1
            else:
                current_length= 1

            longest = max(current_length, longest)
        return longest
