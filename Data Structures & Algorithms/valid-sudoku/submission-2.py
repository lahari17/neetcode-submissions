class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #bruteforce - loop all element search in loop rows, loop cols, oop boxes - O(n3)
        #optimized - created sets for each row, cols, boxes and search each element in them - O(n2)
        n=len(board)
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        box = [set() for _ in range(n)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                
                box_index = (i//3)*3 + (j//3)

                if (board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in box[box_index]):
                    return False

                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                box[box_index].add(board[i][j])
        
        return True
