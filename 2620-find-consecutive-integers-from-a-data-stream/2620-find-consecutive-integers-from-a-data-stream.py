class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.stream = []

    def consec(self, num: int) -> bool:
        if num != self.value:
            self.stream = []
        else:
            self.stream.append(num)
        
        return len(self.stream) >= self.k

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)