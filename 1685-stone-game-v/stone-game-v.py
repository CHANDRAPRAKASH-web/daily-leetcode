class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        f = [[0] * n for _ in range(n)]
        maxl = [[0] * n for _ in range(n)]
        maxr = [[0] * n for _ in range(n)]

        for left in range(n - 1, -1, -1):
            maxl[left][left] = maxr[left][left] = stoneValue[left]
            total = stoneValue[left]
            suml = 0
            i = left - 1
            for right in range(left + 1, n):
                total += stoneValue[right]
                
                # Advance the middle pointer i while left sum <= right sum
                while i + 1 < right and (suml + stoneValue[i + 1]) * 2 <= total:
                    i += 1
                    suml += stoneValue[i]
                
                # Case 1: left sum < right sum (Bob throws right side)
                if left <= i:
                    f[left][right] = max(f[left][right], maxl[left][i])
                
                # Case 2: left sum > right sum (Bob throws left side)
                if i + 1 < right:
                    f[left][right] = max(f[left][right], maxr[i + 2][right])
                
                # Case 3: left sum == right sum (Alice chooses max score)
                if suml * 2 == total:
                    f[left][right] = max(f[left][right], maxr[i + 1][right])
                
                # Update prefix/suffix max arrays for subsequent lookups
                maxl[left][right] = max(maxl[left][right - 1], total + f[left][right])
                maxr[left][right] = max(maxr[left + 1][right], total + f[left][right])

        return f[0][n - 1]