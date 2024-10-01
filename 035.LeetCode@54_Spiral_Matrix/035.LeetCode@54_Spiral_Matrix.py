class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        sizeidx = rows * cols
        arr = []
        startrow, startcol, endrow, endcol, idx = 0, 0, rows - 1, cols - 1, 0
        while startrow <= endrow and startcol <= endcol:
            if idx==sizeidx:
                break
            for i in range (startcol,endcol+1):
                arr.append(matrix[startrow][i])
                idx+=1
            startrow+=1
            if idx==sizeidx:
                break
            for i in range (startrow,endrow+1):
                arr.append(matrix[i][endcol])
                idx+=1
            endcol-=1
            if idx==sizeidx:
                break
            for i in range (endcol,startcol-1,-1):
                arr.append(matrix[endrow][i])
                idx+=1
            endrow-=1
            if idx==sizeidx:
                break
            for i in range (endrow,startrow-1,-1):
                arr.append(matrix[i][startcol])
                idx+=1
            startcol+=1
        return arr