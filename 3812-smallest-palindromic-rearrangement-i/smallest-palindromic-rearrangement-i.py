class Solution:
    def smallestPalindrome(self, s: str) -> str:
       
       p=len(s)//2
       bucket=[0]*26

       for i in range(p):
        bucket[ord(s[i])-ord('a')]+=1

       left="".join(chr(i+ord('a'))*bucket[i] for i in range(26) if bucket[i]>0)

       mid = s[p] if len(s)%2==1 else ""

       right=left[::-1]
       
       return left+mid+right
