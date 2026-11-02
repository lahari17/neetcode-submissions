class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        seen =set()
        for right in range(len(nums)):
            if nums[right] in seen:
                while(nums[right] in seen):
                    seen.remove(nums[left])
                    left = left +1
                if abs((left-1) - right)<= k:
                    return True
            seen.add(nums[right])
        return False
            

