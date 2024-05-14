class Solution:
    # def climbStairs(self, n: int) -> int:
    #     if n == 1:
    #         return 1
    #     elif n == 2:
    #         return 2
    #     return self.climbStairs(n-1) + self.climbStairs(n-2)
    
# Recursive call similar to fibonacci sequence. We know that we can climb stairs in 1 or 2 steps, so we just try to find what the n - 1 and n - 2 steps are
# However this way is 2^n time complexity

# The below solution is O(n)

    def climbStairs(self, n: int) -> int:
        # Initialise array dp of size n + 1 with all elements to 0
        dp = [0] * (n + 1)

        # Base cases
        dp[0] = 1
        dp[1] = 1

        # Iterative step: We iterate from 2 to n to fill the array dp with the number of ways to climb i steps
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]

# Initiate class
calc = Solution()

print(calc.climbStairs(44))