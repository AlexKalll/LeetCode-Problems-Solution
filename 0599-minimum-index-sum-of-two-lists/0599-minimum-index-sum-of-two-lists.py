class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        ht1 = {s: i for i, s in enumerate(list1)}
        ht2 = {s: i for i, s in enumerate(list2)}
        
        min_index_sum = float('inf')
        ans = []

        for s, index1 in ht1.items():
            if s in ht2:
                curr = index1 + ht2[s]
                
                if curr < min_index_sum:
                    min_index_sum = curr
                    ans = [s]  # start a new list with current string
                elif curr == min_index_sum:
                    ans.append(s)  # add to the existing list

        return ans