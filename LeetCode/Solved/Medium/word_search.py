class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    res = self.dfs(board, i, j, 0, word)
                    if res: return res
        return False
            
    def dfs(self, board, i, j, k, word):
        if k == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
            return False
        temp = board[i][j]
        board[i][j] = False
        res = (self.dfs(board, i + 1, j, k + 1, word) or self.dfs(board, i - 1, j, k + 1, word) or 
        self.dfs(board, i, j + 1, k + 1, word) or self.dfs(board, i, j - 1, k + 1, word))
        board[i][j] = temp
        return res