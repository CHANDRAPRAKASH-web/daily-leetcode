class Solution:
    def toLowerCase(self, s: str) -> str:
        h=""
        for i in s:
            h+=i.lower()
        return h