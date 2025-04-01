class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)  
        
        # Fill the DP array from the end to the start
        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            # Option 1: Skip the current question
            dp[i] = dp[i + 1]
            # Option 2: Solve the current question
            next_question = i + brainpower + 1  # Index of the next question after skipping
            if next_question <= n:  # Check if within bounds
                dp[i] = max(dp[i], points + dp[next_question])
            else:
                dp[i] = max(dp[i], points)
        
        return dp[0]  
