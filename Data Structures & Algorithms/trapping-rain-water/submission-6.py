class Solution:
    def trap(self, height: List[int]) -> int:
        # n = len(height)
        # water = 0
        # for i in range(n):
        #     left_max = max(height[:i+1])
        #     right_max = max(height[i:])
        #     water = water + min(left_max,right_max) - height[i]

        # return water


        # n= len(height)
        # left = 0
        # right = n-1
        # water =0
        # left_max =0
        # right_max = 0
        # while left <right:
        #     if height[left]< height[right]:
        #         left_max = max(height[left], left_max)
        #         water = water +  left_max-height[left]
        #         left = left +1
        #     else:
        #         right_max = max(height[right], right_max)
        #         water = water + right_max - height[right]
        #         right = right -1
        # return water
        n = len(height)
        left = 0
        right = n-1
        left_max=0
        right_max=0
        water =0
        while (left<right):
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < right_max:
                water = water + left_max - height[left]
                left = left +1
            else:
                water = water + right_max - height[right]
                right = right - 1
        return water

