class Solution:
    def smallestPalindrome(self, s: str) -> str:
       
       p=len(s)//2
       bucket=[0]*26
       left=""

       for i in range(p):
        bucket[ord(s[i])-ord('a')]+=1

       for i in range(26):
        if bucket[i]>0:
            left+=chr(i+ord('a'))*bucket[i]


       mid = s[p] if len(s)%2==1 else ""

       right=left[::-1]
       
       return left+mid+right
