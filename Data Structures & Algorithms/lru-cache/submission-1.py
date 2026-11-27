class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = {}
        self.order = []

    def get(self, key: int) -> int:
        if key not in self.values:
            return -1

        self.order.remove(key)
        self.order.append(key)

        return self.values[key]
        

    def put(self, key: int, value: int) -> None:

        if key in self.values:
            self.values[key] = value

            self.order.remove(key)
            self.order.append(key)

        else:
            self.values[key] = value
            self.order.append(key)

            if  len(self.values)>self.capacity:
                lru_key = self.order[0]
                self.order.pop(0)
                del self.values[lru_key]



