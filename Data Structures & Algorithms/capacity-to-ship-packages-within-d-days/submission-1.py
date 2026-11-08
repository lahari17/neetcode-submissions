class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        def canShip(capacity):
            days_needed =1
            current_load=0

            for weight in weights:
                if current_load + weight > capacity:
                    days_needed +=1
                    current_load = 0

                current_load +=weight
            return days_needed <=days

        while left<right:
            mid = (left + right)//2
            if canShip(mid):
                right= mid
            else:
                left = mid + 1
        return  left