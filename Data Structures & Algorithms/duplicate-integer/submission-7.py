class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #brute force - check each element with each element in array - O(n2)
        numset = set()
        if len(nums) == len(set(nums)):
            return False
        for num in nums: 
            if num in numset:
                return True
            numset.add(num)