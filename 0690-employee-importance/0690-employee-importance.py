"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        d = {j.id:i for i, j in enumerate(employees)}
        s = [id] #stack
        ans = 0

        while(s):
            curr = s.pop()
            ans += employees[d[curr]].importance
            for child in employees[d[curr]].subordinates:             
                s.append(child)
        return ans