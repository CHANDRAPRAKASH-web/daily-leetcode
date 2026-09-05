class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count=0
        max_count=0
        vowels={'a','e','i','o','u'}
        l=0
        for r in range(len(s)):
            if s[r] in vowels:
                count+=1
            if r>=k-1:
                max_count=max(max_count,count)
                if max_count==k:
                    break
                if s[l] in vowels:
                    count-=1
                l+=1
        return max_count


        