class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #brute force - check each element with each element in array - O(n2)
        if len(nums) == len(set(nums)):
            return False
        return True
