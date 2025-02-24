class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = ListNode()
        self.tail = ListNode()
        self.curr = ListNode(homepage)
        self.head.next = self.curr
        self.curr.prev = self.head
        self.curr.next = self.tail
        self.tail.prev = self.curr

    def visit(self, url: str) -> None:
        temp = ListNode(url)
        temp.prev = self.curr
        self.curr.next = temp
        temp.next = self.tail
        self.tail.prev = temp
        self.curr = temp

    def back(self, steps: int) -> str:
        while steps > 0 and self.curr.prev != self.head:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr.next != self.tail:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
