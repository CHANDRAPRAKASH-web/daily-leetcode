class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        output=set()
        for i in sentence:
            if i not in output:
                output.add(i)
        return len(output)==26