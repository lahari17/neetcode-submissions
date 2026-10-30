class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #bruteforce - sort list then compare each element with next and update lengths and compare - o(nlogn)
        num_set = set(nums)
        longest = 0
        for i in range(len(nums)):
            current = nums[i]
            if current-1 in num_set:
                continue
            length =1
            while current+1 in num_set:
                length +=1
                current +=1
            longest=max(longest, length)
        return longest


        
        