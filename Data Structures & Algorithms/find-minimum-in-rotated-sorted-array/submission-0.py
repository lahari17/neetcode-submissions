class Solution:
    def findMin(self, nums: List[int]) -> int:
        #bruteforce
        minimum = nums[0]
        for num in nums:
            minimum = min(minimum, num)
        return minimum
        
