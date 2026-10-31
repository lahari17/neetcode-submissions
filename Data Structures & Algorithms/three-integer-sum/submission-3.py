class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)):
            target = -nums[i]
            left = i+1
            right = len(nums)-1
            while(left<right):
                if nums[left] + nums[right] == target:
                    lst1=[nums[i],nums[left], nums[right]]
                    if lst1 not in res:
                        res.append([nums[i],nums[left], nums[right]])
                    left=left+1
                    right=right-1
                elif nums[left] + nums[right] <target:
                    left = left +1
                elif nums[left] + nums[right] > target:
                    right = right -1
        return res


            