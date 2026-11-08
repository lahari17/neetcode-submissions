class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def can_split(limit):
            groups = 1
            current_sum = 0

            for num in nums:
                if current_sum + num > limit:
                    groups +=1
                    current_sum = 0
                current_sum +=num
            return groups<=k

        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right)//2

            if can_split(mid):
                right = mid
            else:
                left = mid + 1
        return left