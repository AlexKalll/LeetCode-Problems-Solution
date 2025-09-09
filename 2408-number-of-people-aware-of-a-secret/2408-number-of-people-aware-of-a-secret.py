class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        active_person_counter = 1
        active_spreader = 0
        arr = [0] * n
        arr[0] = 1
        MOD = 10**9 + 7


        for i in range(1,n):
            if i - delay >= 0:
                active_spreader += arr[i - delay]

            if i - forget >= 0:
                active_spreader -= arr[i - forget]
                active_person_counter -= arr[i - forget]
            
            arr[i] = active_spreader
            active_person_counter = (active_person_counter + active_spreader) % MOD
            
        return active_person_counter