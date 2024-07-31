"""
Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if it has a valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array. Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.

Battleship (also Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid containing several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field. The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version. In this kata we will use Soviet/Russian version of the game.

Before the game begins, players set up the board and place the ships accordingly to the following rules:
There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.
Each ship must be a straight line, except for submarines, which are just single cell.
The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner.
"""

def valid_battleship_board(board):
    def mark_ship(x, y):
        # Mark all cells of the current ship and return its length and orientation
        ship_cells = []
        if x < 0 or y < 0 or x >= 10 or y >= 10 or board[x][y] != 1:
            return 0
        stack = [(x, y)]
        while stack:
            i, j = stack.pop()
            if i < 0 or j < 0 or i >= 10 or j >= 10 or board[i][j] != 1:
                continue
            board[i][j] = -1  # Mark as visited
            ship_cells.append((i, j))
            # Check horizontal and vertical neighbors
            stack.append((i + 1, j))
            stack.append((i - 1, j))
            stack.append((i, j + 1))
            stack.append((i, j - 1))
        return ship_cells

    def is_valid_ship(ship_cells):
        if not ship_cells:
            return False
        # Check if all cells are in a line
        if all(x == ship_cells[0][0] for x, y in ship_cells):
            # All x are the same, check consecutive y
            ship_cells.sort(key=lambda cell: cell[1])
            for k in range(1, len(ship_cells)):
                if ship_cells[k][1] != ship_cells[k - 1][1] + 1:
                    return False
        elif all(y == ship_cells[0][1] for x, y in ship_cells):
            # All y are the same, check consecutive x
            ship_cells.sort(key=lambda cell: cell[0])
            for k in range(1, len(ship_cells)):
                if ship_cells[k][0] != ship_cells[k - 1][0] + 1:
                    return False
        else:
            return False
        # Check if any neighboring cells contain another ship
        for x, y in ship_cells:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 10 and 0 <= ny < 10 and board[nx][ny] == 1:
                        return False
        return True

    ship_count = {4: 0, 3: 0, 2: 0, 1: 0}
    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                ship_cells = mark_ship(i, j)
                if not is_valid_ship(ship_cells):
                    return False
                ship_length = len(ship_cells)
                if ship_length in ship_count:
                    ship_count[ship_length] += 1
                else:
                    return False

    return ship_count == {4: 1, 3: 2, 2: 3, 1: 4}

# Example usage
board = [
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

print(valid_battleship_board(board))  # Output: True