class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # nums_dict={}
        # for i, num in enumerate(nums):
        #     if num in nums_dict and (abs(i-nums_dict[num]) <=k):
        #         return True
        #     nums_dict[num] = i
        # return False
        window = set()

        for i, num in enumerate(nums):

            if i>k:
                window.remove(nums[i-k-1])
            if num in window:
                return True
            window.add(num)

        return False
        

        