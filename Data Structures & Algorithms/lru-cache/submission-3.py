class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        self.cache = {}

        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node:Node)->None:
        before = node.prev
        after = node.next

        before.next= after
        after.prev= before

    def _insert_mru(self, node:Node) ->None:
        before = self.right.prev
        before.next = node
        node.prev = before
        node.next = self.right
        self.right.prev = node

    def _move_to_mru(self, node:Node) -> None:
        self._remove(node)
        self._insert_mru(node)
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._move_to_mru(node)

        return node.value


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self._move_to_mru(node)
            return

        node = Node(key, value)
        self.cache[key] = node

        self._insert_mru(node)

        if len(self.cache)>self.capacity:
            lru = self.left.next

            self._remove(lru)
            del self.cache[lru.key]
        
