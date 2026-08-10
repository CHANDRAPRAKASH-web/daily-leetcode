class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp={}

        def dfs(n):
            if n==0:
                return False
            if n in dp:
                return dp[n]

            k=1

            while k*k<=n:
                if not dfs(n-k**2):
                    dp[n]=True
                    return True
                k+=1
            
            dp[n]=False
            return False

        return dfs(n)

                

        
    