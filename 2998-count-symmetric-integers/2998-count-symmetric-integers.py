class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        
        for num in range(low, high + 1):
            str_num = str(num)
            length = len(str_num)
            
            if length % 2 == 0:
                mid = length // 2
                first_half_sum = sum(int(digit) for digit in str_num[:mid])
                second_half_sum = sum(int(digit) for digit in str_num[mid:])
                
                if first_half_sum == second_half_sum:
                    count += 1
        
        return count
