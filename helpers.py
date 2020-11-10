# helper functions

map={
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7
}

# TODO
# use like pieces.KING
pieces={
    'K': "King",
    'Q': "Queen",
    'R': "Rook",
    'N': "Knight",
    'B': "Bishop",
    'p': "Pawn"
}

# returns True if two given cells are on same diagonal
def checkOnSameDiagonal(previousCell, nextCell):

    prevCellCol = map[previousCell[0]]
    prevCellRow = int(previousCell[1])
    prevCellDiff = prevCellCol - prevCellRow

    nextCellCol = map[nextCell[0]]
    nextCellRow = int(nextCell[1])
    nextCellDiff = nextCellCol - nextCellRow

    if (prevCellDiff == nextCellDiff):
        return True
    return False

# returns True if two given cells are on same row
def checkOnSameRow(previousCell, nextCell):
    if(previousCell[1] == nextCell[1]):
        return True
    return False

# returns True if two given cells are on same column
def checkOnSameCol(previousCell, nextCell):
    if (previousCell[0] == nextCell[0]):
        return True
    return False

def switchColor(color):
    if color=='W':
        return 'B'
    else:
        return 'W'

def mapCellToIndex(location):
    desiredCol = location[:1]
    desiredRow = location[1:]

    indexRow = int(desiredRow) - 1
    indexCol = map[desiredCol]

    return [indexRow, indexCol]

def mapIndexToCell(index):
    map=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    row=index[0]+1
    col=map[index[1]]

    return col+str(row)

# return the cell containing a certain piece by searching an entire row
def findCellByRowLocation(board, piece, locationHint):
    for i in range(8):
        col = i
        row = int(locationHint) - 1

        cell = mapIndexToCell([row, col])

        if(board[row][col] == piece):
            return cell
    return False

# return the cell containing a certain piece by searching an entire col
def findCellByColLocation(board, piece, locationHint):
    for i in range(8):
        row= i
        col = map[locationHint]

        cell = mapIndexToCell([row, col])

        if(board[row][col] == piece):
            return cell
    return False