#############################################################
# Determine if a 9 x 9 Sudoku board is valid. 
# Only the filled cells need to be validated 
# according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain 
# the digits 1-9 without repetition.
#############################################################

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # array of 9 sets for rows, cols, and boxes
        # elemets in entered later should be unique

        rows = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        cols = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        boxes = [set(), set(), set(), set(), set(), set(), set(), set(), set()]

        for row in range(9):
            for col in range(9):
                num = board[row][col]

                # continue if number does not exist.
                if num == '.':
                    continue
                
                # check if number is in rows
                # if so return False because their is a duplicate
                # if not add to hash for that row
                if num in rows[row]:
                    return False
                rows[row].add(num)

                # check if number is in cols
                # if so return False because their is a duplicate
                # if not add to hash for that col
                if num in cols[col]:
                    return False
                cols[col].add(num)

                # check if number is in the box
                # modular arithmetic helps find the indecies. 
                # chatgpt assisted me
                # box indexes: [0][0], [0][3], [0][6]
                #                 0       1       2
                #             0 * 3 + 0       0 * 3 + 2
                #              [3][0], [3][3], [3][6]
                #                 3       4       5
                #                     1 * 3 + 1
                #              [6][0], [6][3], [6][6]
                #                 6       7       8 
                #             2 * 3 + 0
                r = (row // 3) * 3
                c = (col // 3)
                i = r + c

                if num in boxes[i]:
                    return False 
                boxes[i].add(num)
        # return true if we make it out the loop
        return True