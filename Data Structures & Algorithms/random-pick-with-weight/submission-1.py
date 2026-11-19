class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        running_total = 0
        for weight in w:
            running_total = running_total + weight
            self.prefix.append(running_total)

    def pickIndex(self) -> int:
        ticket = random.randint(1, self.prefix[-1])

        left = 0
        right = len(self.prefix) - 1

        while left < right:
            mid = (left+right)//2
            if self.prefix[mid]>=ticket:
                right = mid
            else:
                left = mid + 1
        return left



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()