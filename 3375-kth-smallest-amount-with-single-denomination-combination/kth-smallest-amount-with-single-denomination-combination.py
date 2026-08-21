class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(coins)
        subsets = []
        
        for i in range(1, 1 << n):
            c = 0
            cur_lcm = 1
            for j in range(n):
                if (i >> j) & 1:
                    c += 1
                    cur_lcm = (cur_lcm * coins[j]) // gcd(cur_lcm, coins[j])
            
            subsets.append((cur_lcm, 1 if c % 2 != 0 else -1))

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2
            count = sum(sign * (mid // val) for val, sign in subsets)
            
            if count >= k:
                right = mid
            else:
                left = mid + 1

        return left