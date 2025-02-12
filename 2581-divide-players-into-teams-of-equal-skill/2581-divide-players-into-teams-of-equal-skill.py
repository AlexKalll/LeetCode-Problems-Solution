class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        team_skill = skill[0] + skill[-1]
        l, r = 1, len(skill) - 2

        ans = skill[0] * skill[-1]

        while l < r:
            curr = skill[l] + skill[r]
            if curr != team_skill:
                return -1
                
            ans += skill[l] * skill[r]
            l += 1
            r -= 1
        
        return ans 