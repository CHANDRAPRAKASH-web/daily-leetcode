class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m=float('inf')

        for s in strs:
            if len(s) < m:
                m=len(s)
        
        i=0

        while i<m:
            for s in strs:
                if s[i]!=strs[0][i]:
                    return s[:i]

            i+=1


        return s[:i]

        



        