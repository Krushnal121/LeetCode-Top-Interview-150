class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        length = len(matrix)
        for i in range (length):
            for j in range (i,length):
                temp=matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for i in range (length):
            for j in range (length//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][length-1-j]
                matrix[i][length-1-j] = temp