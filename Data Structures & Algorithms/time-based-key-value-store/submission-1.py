class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp,value))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        entries = self.store[key]

        left = 0
        right = len(entries)

        while left < right:
            mid = (left + right)//2
            if entries[mid][0] <=timestamp:
                left = mid + 1
            else:
                right = mid
        index = left - 1

        if index<0:
            return ""

        return entries[index][1]
        




        
