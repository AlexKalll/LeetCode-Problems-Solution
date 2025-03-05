class RecentCounter:

    def __init__(self):
        self.count = 0
        self.q = []
        self.i = 0

    def ping(self, t: int) -> int:
        
        self.q.append(t)
        self.count += 1
        
        while self.q[self.count-1] - self.q[self.i] > 3000:
            self.i += 1
        
        return self.count - self.i


        

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)