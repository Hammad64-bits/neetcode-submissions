class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        n = len(board)
        
        for i in range(n):

            # check row
            map = {}
            for j in range(n):
                if board[i][j] == '.': continue
                if board[i][j] in map: return False
                map[board[i][j]] = True

            # check col
            map = {}
            for j in range(n):
                if board[j][i] == '.': continue
                if board[j][i] in map: return False
                map[board[j][i]] = True

            # column check
            # map = {}
            # for j in range(n):
            #     if board[i][j] == '.': continue
            #     if board[i][j] in map: return False
            #     map[board[j][i]] = True
         
            map = {}
            box_row = i // 3 
            box_col = i % 3
            start_row = box_row * 3
            start_col = box_col * 3
            for j in range(3):
               for k in range(3):
                    if board[start_row + j][start_col + k] == '.': continue
                    if board[start_row + j][start_col + k] in map:
                         return False
                    map[board[start_row + j][start_col + k]] = True
           

        return True
