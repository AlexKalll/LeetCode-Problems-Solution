class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def can_partition(num, target):
            # invalid partiion found 
            if target < 0 or num < target:
                return False
            
            # if valid
            if num == target:
                return True
            # recursive check all partitions for a valid partition
            return (can_partition(num//10, target-num % 10) or can_partition(num//100, target-num % 100) or can_partition(num//1000, target - num % 1000))


        punishment_num = 1 # since 1 is can be partititons as '1'

        for curr_num in range(2, n + 1):
            square_num = curr_num **2

            # check if valid partition can be found and add squared num if it is valid 
            if can_partition(square_num, curr_num):
                punishment_num += square_num
        
        return punishment_num