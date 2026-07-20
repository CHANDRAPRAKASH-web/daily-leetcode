class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>len(magazine):
            return False

        return not (Counter(ransomNote)-Counter(magazine))
       