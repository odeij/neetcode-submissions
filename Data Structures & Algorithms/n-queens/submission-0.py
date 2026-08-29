class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        pos = [0] * n

        def is_safe(column: int, row: int) -> bool:
            for prev_col in range(column):
                if pos[prev_col] == row:
                    return False

                if pos[prev_col] + prev_col == row + column:
                    return False

                if pos[prev_col] - prev_col == row - column:
                    return False

            return True

        def create_board():
            board = []

            for column in range(n):
                row = pos[column]

                line = ["."] * n
                line[row] = "Q"

                board.append("".join(line))

            return board

        def solve(column: int):
            if column == n:
                result.append(create_board())
                return

            for row in range(n):
                if is_safe(column, row):
                    pos[column] = row
                    solve(column + 1)

        solve(0)

        return result
        