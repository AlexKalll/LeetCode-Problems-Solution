class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # floyd's tort and hare approach for cycle detection and finding entrance node ( fast & slow pointers approach)
        hare = tort = 0

        while True:
            hare = nums[nums[hare]]
            tort = nums[tort]

            if tort == hare:
                tort = 0

                while tort != hare:
                    tort = nums[tort]
                    hare = nums[hare]

                return tort