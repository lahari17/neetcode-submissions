class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for i,j in counter.items():
            if j>1:
                return True
            
        return False

# Space complexity = O(N)
# Time Complexity
# Counter() = O(N)
# for loop = O(M)
# Total time = O(N)
