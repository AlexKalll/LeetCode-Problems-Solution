class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} 
        self.head = ListNode()  
        self.tail = ListNode()  
        self.head.next = self.tail
        self.tail.prev = self.head
        self.n = 0
    # 
    def delete_node(self, node: ListNode):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    # put the most recently used to the front 
    def add_to_front(self, node: ListNode):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.delete_node(node)
            self.add_to_front(node)
            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.delete_node(node)
            node.val = value
            self.add_to_front(node)
        else:
            if self.n == self.capacity: # if full of capacity is used, evict the last
                last_node = self.tail.prev
                self.delete_node(last_node)
                del self.cache[last_node.key]
                self.n -= 1
            
            # add the new node to the front since it is gonna be MRU(most recently used)
            temp = ListNode(key, value)
            self.cache[key] = temp
            self.add_to_front(temp)
            self.n += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)