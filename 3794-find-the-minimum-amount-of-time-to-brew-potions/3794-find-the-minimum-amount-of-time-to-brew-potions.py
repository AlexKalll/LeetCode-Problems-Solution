class Solution:
    def minTime(self, skills: List[int], mana: List[int]) -> int:
        n_wizards = len(skills)
        # times[w] stores the time wizard w finishes the PREVIOUS potion
        times = [0] * n_wizards

        for mana_point in mana:
            # --- FORWARD PASS: Compute last wizard's finish time, allowing for gaps ---
            # cur_time represents the finish time of the CURRENT potion as it passes
            # through the wizards.
            cur_time = 0
            for w in range(n_wizards):
                # Wizard w can only start the current potion after they are free (times[w])
                # AND after the potion arrives from wizard w-1 (cur_time).
                start_time = max(cur_time, times[w])
                cur_time = start_time + skills[w] * mana_point

            # --- BACKWARD PASS: Eliminate gaps to enforce synchronized handoffs ---
            # We now have the correct finish time for the last wizard.
            times[n_wizards - 1] = cur_time
            # Work backwards to find the required finish time for each preceding wizard.
            for w in range(n_wizards - 2, -1, -1):
                # Wizard w must finish exactly when wizard w+1 starts.
                # Start time for w+1 = finish_time[w+1] - processing_time[w+1]
                times[w] = times[w + 1] - skills[w + 1] * mana_point
        
        return times[-1]