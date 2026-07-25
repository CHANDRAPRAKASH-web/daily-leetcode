class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            sett=set()
            for j in range(9):
                value=board[i][j]
                if value in sett:
                    return False
                elif value!=".":
                    sett.add(value)

        for i in range(9):
            sett=set()
            for j in range(9):
                value=board[j][i]
                if value in sett:
                    return False
                elif value!=".":
                    sett.add(value)
        start=[(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]

        for i,j in start:
            sett=set()
            for a in range(i,i+3):
                for b in range(j,j+3):
                    value=board[a][b]
                    if value in sett:
                        return False
                    elif value!=".":
                        sett.add(value)

       

        return True

        

        