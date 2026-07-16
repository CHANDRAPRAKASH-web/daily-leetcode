class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        for i in words:
            l=0
            r=len(i)-1
            temp=1
            while l < r:
                if i[l]!=i[r]:
                    temp=0
                    break
                l+=1
                r-=1
            if temp==1:
                return i
        return ""