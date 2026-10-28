class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #bruteforce - for each number check entire array to check for remaing diff value - O(n2) 
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen.get(diff), i]
            seen[nums[i]] = i

#Time = O(n)
#Space= O(n)