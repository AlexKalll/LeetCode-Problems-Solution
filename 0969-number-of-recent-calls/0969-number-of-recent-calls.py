class RecentCounter:

    def __init__(self):
        self.q = []
        self.i = 0

    def ping(self, t: int) -> int:
        self.q.append(t)
        
        while self.q[len(self.q)-1] - self.q[self.i] > 3000:
            self.i += 1
        
        return len(self.q) - self.i


        

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)