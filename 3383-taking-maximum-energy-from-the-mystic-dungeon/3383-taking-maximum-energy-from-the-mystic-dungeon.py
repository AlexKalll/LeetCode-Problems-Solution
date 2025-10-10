class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        max_energy = float('-inf')
        n = len(energy)
        
        # Iterate backwards through the array
        for i in range(n - 1, -1, -1):
            # If there's a next position in the chain, add its accumulated energy
            if i + k < n:
                energy[i] += energy[i + k]
            # Update maximum energy found so far
            max_energy = max(max_energy, energy[i])
        
        return max_energy