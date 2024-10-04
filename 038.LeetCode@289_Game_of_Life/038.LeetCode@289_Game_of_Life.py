class Solution:
    def gameOfLife(self, board) -> None:
        if not board or len(board) == 0:
            return
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                lives = self.lives(board, m, n, i, j)
                if board[i][j] == 1 and 2 <= lives <= 3:
                    board[i][j] = 3
                elif board[i][j] == 0 and lives == 3:
                    board[i][j] = 2
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1

    def lives(self, board, m, n, i, j) -> int:
        lives = 0
        for x in range(max(0, i - 1), min(m , i + 2)):
            for y in range(max(0, j - 1), min(n, j + 2)):
                lives += board[x][y] & 1
        lives -= board[i][j] & 1
        return lives
