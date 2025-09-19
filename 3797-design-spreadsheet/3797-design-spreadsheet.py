class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows 
        self.ht = defaultdict(int)
        
    def setCell(self, cell: str, value: int) -> None:
        self.ht[cell] = value

    def resetCell(self, cell: str) -> None:
        self.ht[cell] = 0

    def getValue(self, formula: str) -> int:
        operands = formula[1:].split('+')
        ans = 0
        if operands[0].isdigit():
            ans += int(operands[0])
        else:
            ans += self.ht[operands[0]]
            
        if operands[1].isdigit():
            ans += int(operands[1])
        else:
            ans += self.ht[operands[1]]

        return ans


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)