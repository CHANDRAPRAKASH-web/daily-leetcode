class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        a=[]
        for i,val in enumerate(words):
            if x in val:
                a.append(i)


        return a

        