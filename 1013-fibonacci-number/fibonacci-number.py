class Solution:
    def fib(self, n: int) -> int:
        memo={0:0,1:1}

        def f(x):
            if x in memo:
                return memo[x]
            memo[x]=f(x-2)+f(x-1)
            return memo[x]

        return f(n)

        