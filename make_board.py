def create_board(dim):
    board = []
    for x in range(dim):
        row = []
        for y in range(dim):
            row.append(".")
        board.append(row)
    return board

def coord_map(board):
    grid = []
    for x in range(len(board)):
        row = []
        for y in range(len(board)):
            row.append((x, y))
        grid.append(row)
    return grid

def groups_to_check(board):
    result = []
    for row in board:
        result.append(row)
    for row in board:
        col = []
        for item in row:
            col.append((item[1], item[0]))
        result.append(col)
    diag_1 = []
    diag_2 = []
    a = 0
    b = len(board) - 1
    for i in range(len(board)):
        diag_1.append((i, i))
        diag_2.append((a, b))
        a += 1
        b -= 1
    result.append(diag_1)
    result.append(diag_2)
    return result


# min arg is 2
dim = 5
board = create_board(dim)
print(f"\nBoard of dimension {dim} x {dim} \n")
for x in board:
    print(x, "\n")
coords = coord_map(board)
print(f"\nMap of board coordinates\n")
for x in coords:
    print(x, "\n")
print(f"\nGroups to check\n")
# for x in groups_to_check(coords):
#     print(x, "\n")
print(groups_to_check(coords))
