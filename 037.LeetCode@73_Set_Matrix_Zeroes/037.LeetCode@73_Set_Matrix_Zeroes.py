class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        flagrow=False
        flagcol=False

        for i in range(len(matrix)):
            if(matrix[i][0] == 0):
                flagrow=True
                break

        for i in range(len(matrix[0])):
            if(matrix[0][i] == 0):
                flagcol=True
                break

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if (matrix[i][j] == 0):
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if (matrix[i][0] == 0 or matrix[0][j] ==0):
                    matrix[i][j] = 0

        if (flagrow):
            for i in range(len(matrix)):
                matrix[i][0] = 0

        if(flagcol):
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
