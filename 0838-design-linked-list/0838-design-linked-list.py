class ListNone:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.dummy = ListNode()
  

    def get(self, index: int) -> int:
        curr = self.dummy
        count = 0
        while curr and count < index: # since it is a 0-indexed 
            curr = curr.next
            count += 1

        if curr and curr.next:
            return curr.next.val
        else:
            return -1
        


    def addAtHead(self, val: int) -> None:
        temp = ListNode(val)
        if not self.dummy.next:
            self.dummy.next = temp
        else:
            temp.next = self.dummy.next
            self.dummy.next = temp
           

    def addAtTail(self, val: int) -> None:
        curr = self.dummy 
        temp = ListNode(val)
        while curr.next:
            curr = curr.next
        
        curr.next = temp


    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.dummy 
        count = 0

        while curr and count < index:
            curr = curr.next
            count += 1

        if count == index and curr:
            temp = ListNode(val)
            
            temp.next = curr.next 
            curr.next = temp
            
        
        # print(self.dummy.next)
        
    def deleteAtIndex(self, index: int) -> None:
        curr = self.dummy
        count = 0
        
        while curr and count < index:
            curr = curr.next
            count += 1
        
        if count == index and curr and curr.next:
            curr.next = curr.next.next

        # print(self.dummy.next)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)