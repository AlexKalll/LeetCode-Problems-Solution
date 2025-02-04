class RandomizedSet:
    def __init__(self):
        self.index_map = {}
        self.lists = []

    def insert(self, val: int) -> bool:
        if val not in self.index_map:
            self.index_map[val] = len(self.lists)
            self.lists.append(val)
            return True

        return False

    def remove(self, val: int) -> bool:
        if val in self.index_map:
            remove_idx = self.index_map[val]
            last_val = self.lists[-1]
            self.index_map[last_val] = remove_idx
            self.lists[remove_idx], self.lists[-1] = self.lists[-1], self.lists[remove_idx]
            del self.index_map[val]
            self.lists.pop()
            return True

        return False
            

    def getRandom(self) -> int:  
        return choice(self.lists)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()