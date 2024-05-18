class ListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # Dummy nodes to mark the beginning and end of the linked list
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_front(self, node):
        # Move a node to the front of the linked list
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.move_to_front(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_to_front(node)
        else:
            if len(self.cache) == self.capacity:
                # Evict the least recently used node (from the end of the linked list)
                del self.cache[self.tail.prev.key]
                self.tail.prev = self.tail.prev.prev
                self.tail.prev.next = self.tail
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            new_node.next = self.head.next
            new_node.prev = self.head
            self.head.next.prev = new_node
            self.head.next = new_node

# Example usage:
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # Output: 1
cache.put(3, 3)
print(cache.get(2))  # Output: -1
cache.put(4, 4)
print(cache.get(1))  # Output: -1
print(cache.get(3))  # Output: 3
print(cache.get(4))  # Output: 4
