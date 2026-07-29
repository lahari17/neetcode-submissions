class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2*n)
        for i in range(2 * n):
            if i < n:
                ans[i] = nums[i]
            elif n <= i < 2 * n:
                ans[i] = nums[i % n]

        return ans

#len(nums)- O(1)
# [0]*(2*n) - O(2n)
# for loop - O(2n)

# Total time- O(4n)=O9n)
# Space- O(2n)