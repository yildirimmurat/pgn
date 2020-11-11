# helper functions
import numpy as np


# 2D board array
# https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
rows, cols = (8, 8) 
board = [['--' for i in range(rows)] for j in range(cols)]

savedLocations = {}


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
pieces = {
    'KING': 'K',
    'QUEEN': 'Q',
    'ROOK': 'R',
    'KNIGHT': 'N',
    'BISHOP': 'B',
    'PAWN': 'p'
}

# can be used several times
colors = {
    'WHITE' : 'W',
    'BLACK': 'B'
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
    if color == colors['WHITE']:
        return colors['BLACK']
    else:
        return colors['WHITE']

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

# return the piece that is on the cell
def getCellValue(board, cell):
    index = mapCellToIndex(cell)
    return board[index[0]][index[1]]

# return the color of cell
def getCellColor(cell):
    index=mapCellToIndex(cell)
    if (index[0]+index[1]) % 2 == 0:
        return colors['WHITE']
    else:
        return colors['BLACK']

# return saved locations of the given piece
def findSavedCellLocation(piece):
    return savedLocations[piece]

# make cell empty
def emptyCell(previousCell):
    previousIndex = mapCellToIndex(previousCell)
    piece=board[previousIndex[0]][previousIndex[1]]

    # https://stackoverflow.com/questions/10996140/how-to-remove-specific-elements-in-a-numpy-array
    a = np.array(savedLocations[piece])
    b = np.array([previousCell])
    savedLocations[piece] = np.setdiff1d(a, b)
    board[previousIndex[0]][previousIndex[1]] = '--'

    return

# fill cell with a given piece
def fillCell(nextCell, piece):
    nextIndex = mapCellToIndex(nextCell)
    board[nextIndex[0]][nextIndex[1]] = piece

    # https://stackoverflow.com/questions/9775297/concatenate-a-numpy-array-to-another-numpy-array
    a = np.array([nextCell])
    b = savedLocations[piece]
    savedLocations[piece]=np.concatenate((a, b))

    # print(savedLocations)

    return

