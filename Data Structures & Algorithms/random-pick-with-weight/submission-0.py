class Solution:

    def __init__(self, w: List[int]):
        self.weights = w
        self.total = sum(w)

    def pickIndex(self) -> int:
        ticket = random.randint(1, self.total)

        running_sum = 0
        for i, weight in enumerate(self.weights):
            running_sum = running_sum+weight

            if running_sum >=ticket:
                return i
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()