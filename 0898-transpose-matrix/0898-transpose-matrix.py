class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        # Zip function will take one element from each element of the martix and make them tuple and return these tuples
        transposed_tuple = zip(*matrix) 
        
        for row in transposed_tuple:
            ans.append(list(row))
        
        return ans