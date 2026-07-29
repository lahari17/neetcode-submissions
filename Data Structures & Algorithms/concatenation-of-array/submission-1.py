class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums + nums

        return ans

#space- O(2n)=O(n)
#time - O(n+n)=O(2n)=O(n)