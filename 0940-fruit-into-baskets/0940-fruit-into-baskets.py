class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, max_len = 0, 0
        fruit_count = defaultdict(int)

        for right, fruit in enumerate(fruits):
            fruit_count[fruit] += 1

            while len(fruit_count) > 2:
                fruit_count[fruits[left]] -= 1
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len