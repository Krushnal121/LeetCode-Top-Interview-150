class Solution:
    def searchMatrix(self, matrix, target):
        row = 0
        length = len(matrix)
        col = len(matrix[0]) - 1

        while row < length and col >= 0:
            if matrix[row][col] == target:
                return True
            elif target < matrix[row][col]:
                col -= 1
            else:
                row += 1
        return False
