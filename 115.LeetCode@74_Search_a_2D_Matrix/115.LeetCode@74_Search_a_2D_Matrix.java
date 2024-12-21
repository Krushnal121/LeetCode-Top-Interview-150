class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int row = 0;
        int length = matrix.length;
        int col = matrix[0].length - 1;

        while (row < length && col >= 0) {
            if (matrix[row][col] == target) {
                return true;
            } else if (target < matrix[row][col]) {
                col--;
            } else {
                row++;
            }
        }
        return false;
    }
}