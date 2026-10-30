class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=1
        suffix = 1
        prefix_array=[0]*len(nums)
        suffix_array=[0]*len(nums)
        result=[0]*len(nums)
        for i in range(len(nums)):
            prefix_array[i]=prefix
            prefix = prefix * nums[i]

        for i in range(len(nums)-1, -1, -1):
            suffix_array[i]=suffix
            suffix = suffix * nums[i]

        for i in range(len(nums)):
            result[i] = prefix_array[i] * suffix_array[i]

        return result
            

