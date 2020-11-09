#!/usr/bin/python3
import sys
import re
import cs50
from analyseSingleMove import makeMove
import numpy as np

# put all pieces into default positions
    # TODO all pieces should have property of eliminated=True or eliminated=False 
    # all big pieces should have its saved cells
        # 2 knights ( can be differentiated by their saved locations) --- knight1Cell & knight2Cell
        # 2 bishops ( can be differentiated by white and black)---so whiteBishopCell & blackBishopCell
    # cells can be empty or full according to moves
    # TODO --> en passant for pawns
    # TODO --> queen upgrade for pawns

# from a single game
# select the game from  db
# read moves from db
# for each move analyse move
# print result


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

pieces={
    'K': "King",
    'Q': "Queen",
    'R': "Rook",
    'N': "Knight",
    'B': "Bishop",
    'p': "Pawn"
}

def main():
    printBoard()
    putPiecesIntoDefaultPosition()
    printBoard()

    # piece='Wp'
    # loc=showLocation(piece)
    # print(loc)

    #readSingleGameFromDB()
    #readMovesFromGame()

    color="B"
    moveList=['e4', 'e5', 'O-O', 'O-O-O', 'axb3', 'Qxe4', 'Bxe5', 'Bxe4', 'Rxa7', 'c5', 'Rxb7']
    for i in range(len(moveList)):
        color=switchColor(color)
        print('color is: ', color)
        print('move is: ', moveList[i])
        move=moveList[i]
        output=makeMove(move, color)
        print('output:')
        print(output)

        l=len(output['piece'])
        if l > 1:
            for i in range(l):
                piece=color+output['piece'][i]
                previousCell=output['previousCell'][i]
                nextCell=output['nextCell'][i]
                emptyCell(previousCell)
                fillCell(nextCell, piece)

        elif (isinstance(output['previousCell'], list)):
            # e.g for e4 move previous cell could be both e5 or e6
            
            piece=color+output['piece']
            for i in range(len(output['previousCell'])):
                cell = output['previousCell'][i]
                index = mapCellToIndex(cell)
                if (board[index[0]][index[1]] != '--'):
                    previousCell = cell
                    break
            nextCell=output['nextCell']
            emptyCell(previousCell)
            fillCell(nextCell, piece)
            
        elif(output['previousCell'] == 'previousCell'):
            piece=color+output['piece']
            nextCell=output['nextCell']


            print('do the work')
            previousCell=findSavedCellLocation(piece, nextCell)
            if (len(previousCell) == 1):
                previousCell = previousCell[0]
            elif (piece[1]=='B'):
                nextColor = getCellColor(nextCell)
                if (nextColor == getCellColor(previousCell[0])):
                    previousCell = previousCell[0]
                else:
                    previousCell = previousCell[1]
            elif (piece[1]=='R'):
                # should check if they can capture the piece
                # there can be also more than two rooks on board
                for i in range(len(previousCell)):
                    print('i', i)
                    capture=canCapture(piece[1], previousCell[i], nextCell)
                    
                    print('in capture', capture)
                    if capture:
                        previousCell = previousCell[i]
                        break
            elif (piece[1]=='Q'):
                for i in range(len(previousCell)):
                    capture=canCapture(piece[1], previousCell[i], nextCell)
                    if capture:
                        previousCell = previousCell[i]
                        break
                

            

            print('previousCell')
            print(previousCell)


            emptyCell(previousCell)
            fillCell(nextCell, piece)

        else:
            piece=color+output['piece']
            previousCell=output['previousCell']
            nextCell=output['nextCell']
            emptyCell(previousCell)
            fillCell(nextCell, piece)



        printBoard()

    printBoard()
    print(checkPieceInDiagonal('h2', 'b8'))

# return true if type of a piece can capture the cell from a prev. cell
def canCapture(piece, previousCell, nextCell):
    if (piece == 'R'):
        if (previousCell[0] == nextCell[0]):
            # same col
            # check if any piece in between
            prevRow = int(previousCell[1])
            nextRow = int(nextCell[1])

            if (abs(nextRow-prevRow) == 1):
                # adjacent cells
                return True
            else: 
                for i in range(prevRow, nextRow-1):
                    col = map[previousCell[0]]
                    if (board[i][col] != '--'):
                        return False
                return True

        elif (previousCell[1] == nextCell[1]):
            # same row
            # check if any piece in between
            prevCol = previousCell[0]
            nextCol = nextCell[0]

            if (abs(map[nextCol]-map[prevCol]) == 1):
                # adjacent cells
                return True
            else:
                for i in range(prevCol, nextCol-1):
                    row = previousCell[1]
                    # print('board[row][:',i,']:', board[row][i])
                    if (board[i][col] != '--'):
                        return False
                return True


            return False
        else:
            return False

    elif (piece=='Q'):
        # if has on same diagonal or same row or same col
        sameDiagonal = checkOnSameDiagonal(previousCell, nextCell)
        sameRow = checkOnSameRow(previousCell, nextCell)
        sameCol = checkOnSameCol(previousCell, nextCell)

        if sameRow:
            if checkPieceInRow(previousCell, nextCell):
                return True
            return False
        elif sameCol:
            if checkPieceInCol(previousCell, nextCell):
                return True
            return False
        elif sameDiagonal:
            if checkPieceInDiagonal(previousCell, nextCell):
                return True
            return False
        else:
            return False
        

# returns True if two given cells are on same diagonal
def checkSameDiagonal(previousCell, nextCell):

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

# returns False if there is no piece between cells which are on same row
def checkPieceInRow(previousCell, nextCell):

    row = int(previousCell[1]) - 1

    prevCol = map[previousCell[0]]
    nextCol = map[nextCell[0]]

    if (prevCol > nextCol):
        prevCol, nextCol = nextCol, prevCol

    # CHECK IF adjacent cells
    if(nextCol - prevCol == 1):
        return False
    else:
        for i in range(prevCol + 1, nextCol):
            searchIndex = [row, i]
            cell = mapIndexToCell(searchIndex)
            val = getCellValue(cell)
            if (val != '--'):
                return True
        return False

# returns False if there is no piece between cells which are on same col
def checkPieceInCol(previousCell, nextCell):
    
    col = map[previousCell[0]]

    prevRow = int(previousCell[1]) - 1
    nextRow = int(nextCell[1]) - 1

    if (prevRow > nextRow):
        prevRow, nextRow = nextRow, prevRow

    # CHECK IF adjacent cells
    if(nextRow - prevRow == 1):
        return False
    else:
        for i in range(prevRow + 1, nextRow):
            searchIndex = [i, col]
            cell = mapIndexToCell(searchIndex)
            val = getCellValue(cell)
            if (val != '--'):
                return True
        return False           

# returns False if there is no piece between cells which are on same diagonal
def checkPieceInDiagonal(previousCell, nextCell):
    
    prevRow = int(previousCell[1]) - 1
    nextRow = int(nextCell[1]) - 1

    prevCol = map[previousCell[0]]
    nextCol = map[nextCell[0]]

    toUp = 1
    if (prevRow > nextRow):
        prevRow, nextRow = nextRow, prevRow
        prevCol, nextCol = nextCol, prevCol
    if(prevCol > nextCol):
        # if previous cell is on the upper part of the board, then go downwards while searching
        toUp = -1

    # CHECK IF adjacent cells
    if(nextRow - prevRow == 1):
        return False
    else: 
        col = prevCol
        for i in range(prevRow + 1, nextRow):
            col = col + toUp
            searchIndex = [i, col]
            cell = mapIndexToCell(searchIndex)
            val = getCellValue(cell)
            if (val != '--'):
                return True
        return False

def getCellValue(cell):
    index = mapCellToIndex(cell)
    return board[index[0]][index[1]]

def getCellColor(cell):
    index=mapCellToIndex(cell)
    if (index[0]+index[1]) % 2 == 0:
        return 'light'
    else:
        return 'dark'


def findSavedCellLocation(piece, nextCell):
    return savedLocations[piece]


def switchColor(color):
    if color=='W':
        return 'B'
    else:
        return 'W'

def emptyCell(previousCell):
    previousIndex = mapCellToIndex(previousCell)
    piece=board[previousIndex[0]][previousIndex[1]]

    # https://stackoverflow.com/questions/10996140/how-to-remove-specific-elements-in-a-numpy-array
    a = np.array(savedLocations[piece])
    b = np.array([previousCell])
    savedLocations[piece] = np.setdiff1d(a, b)
    board[previousIndex[0]][previousIndex[1]] = '--'



    return

def fillCell(nextCell, piece):
    nextIndex = mapCellToIndex(nextCell)
    board[nextIndex[0]][nextIndex[1]] = piece

    # https://stackoverflow.com/questions/9775297/concatenate-a-numpy-array-to-another-numpy-array
    a = np.array([nextCell])
    b = savedLocations[piece]
    savedLocations[piece]=np.concatenate((a, b))


    print('..............')
    print('filling ', nextCell,'location')
    print('savedLocations...')
    print(savedLocations)
    print('............')


    return

   
def mapCellToIndex(location):
    global board
    global map
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

# puts a piece into a desired location on the board
def putPieceIntoBoard(piece, location):
    global board

    index=mapCellToIndex(location)
    row=index[0]
    col=index[1]
    board[row][col] = piece


    return
    

def putPieceIntoBoardByArray(arr):
    for i in range(len(arr)):
        piece=arr[i][0]
        location=arr[i][1]
        putPieceIntoBoard(piece, location)
    
    return


def putPiecesIntoDefaultPosition():
    # default position
    # first letter is whether it is (W)hite or (B)lack
    # second letter is about type of piece (Q):Queen etc.    putPieceIntoBoard('BR', 'a8')
    putPieceIntoBoardByArray([['BR', 'a8'], ['BN', 'b8'], ['BB', 'c8'], ['BQ', 'd8'], ['BK', 'e8'], ['BB', 'f8'], ['BN', 'g8'], ['BR', 'h8']])
    putPieceIntoBoardByArray([['Bp', 'a7'], ['Bp', 'b7'], ['Bp', 'c7'], ['Bp', 'd7'], ['Bp', 'e7'], ['Bp', 'f7'], ['Bp', 'g7'], ['Bp', 'h7']])
    putPieceIntoBoardByArray([['Wp', 'a2'], ['Wp', 'b2'], ['Wp', 'c2'], ['Wp', 'd2'], ['Wp', 'e2'], ['Wp', 'f2'], ['Wp', 'g2'], ['Wp', 'h2']])
    putPieceIntoBoardByArray([['WR', 'a1'], ['WN', 'b1'], ['WB', 'c1'], ['WQ', 'd1'], ['WK', 'e1'], ['WB', 'f1'], ['WN', 'g1'], ['WR', 'h1']])
    
    savedLocations['BR']=['a8', 'h8']
    savedLocations['BN']=['b8', 'g8']
    savedLocations['BB']=['c8', 'f8']
    savedLocations['BQ']=['d8'] # saved as an array because afterwards pawns could promote
    savedLocations['BK']=['e8']
    savedLocations['Bp']=['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7']

    savedLocations['WR']=['a1', 'h1']
    savedLocations['WN']=['b1', 'g1']
    savedLocations['WB']=['c1', 'f1']
    savedLocations['WQ']=['d1'] # saved as an array because afterwards pawns could promote
    savedLocations['WK']=['e1']
    savedLocations['Wp']=['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']

    return


def printBoard():
    print("=================================")
    for i in range(8):
        print(board[8-i-1])
    print("=================================")


def showLocation(piece):#todo searchIn -- whole board or just white-black squares, how many piece there are currently
    locationArr=[]
    for i in range(8):
        for j in range(8):
            if(board[i][j]==piece):
                index=[i, j]
                cell=mapIndexToCell(index)
                locationArr.append(cell)

    return locationArr

def readSingleGameGromDB():
    print("reading single game from database")

def readMovesFromGame():
    print("reading moves from game")




main()