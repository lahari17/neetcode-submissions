class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lst=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target = -nums[i]
            l=i+1
            r=len(nums)-1
            while(l<r):
                if nums[l]+nums[r]==target:
                    lst.append([nums[l], nums[r],nums[i]])
                    l=l+1
                    r=r-1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                if nums[l]+nums[r]< target:
                    l=l+1

                if nums[l]+nums[r]> target:
                    r=r-1
        return lst
#Time=O(nlogn)+O(n2)
#Space=O(n2)
