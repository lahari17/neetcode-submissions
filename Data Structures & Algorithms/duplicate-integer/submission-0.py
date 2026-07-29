class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if ( len(set(nums))==len(nums)):
            return False
        else:
            return True


#Space complexity - O(n)
#Time Complexity - 
# set(nums) - O(n)
# len of set and list - O(1)

# Total time = O(n)
        