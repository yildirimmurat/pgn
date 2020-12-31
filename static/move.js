"use strict"
import Playground from './Playground.js';
// import analyseMove from './analyseMove.js';
// import {board, colors} from './definitions.js'


window.move = function(color, output) {

    if(output.takes == true) {
        Playground.removeFigure(output.nextCell)
    }

    if(output['piece'].length == 2) {
        castle(color, output)
    } else if(Array.isArray(output['previousCell'])) {
        possibleFirstPawnMove(color, output, board)
    } else if(output['previousCell'] == 'previousCell') {
        makeMoveFromSavedLocation(color, output, board)
    } else {
        makeMoveByGivenLocation(color, output, board)
    }

    if(output['promotion'] != '') {
        console.log('in promote')
        promote(output['nextCell'], color, output['promotion'])
    }

    console.log('prev: ' + output.previousCell + ' next: ' + output.nextCell)
    Playground.highlightMove(output.previousCell, output.nextCell)
}

const castle = function(color, output) {
    for(let i = 0; i < 2; i++) {
        let piece=color+output['piece'][i]
        let previousCell=output['previousCell'][i]
        let nextCell=output['nextCell'][i]
        captureCell(piece, previousCell, nextCell)
        Playground.moveFigure(previousCell, nextCell);
    }
    return
}

// capture a cell by piece
const captureCell = function(piece, previousCell, nextCell) {
    emptyCell(previousCell)
    fillCell(nextCell, piece)

    return
}

// make possible first move
const possibleFirstPawnMove = function(color, output, board) {
    // e.g for e4 move previous cell could be both e3 or e2
    // TODO problem when both e3 and e2 are occupied by a pawn
    
    let piece=color+output['piece']
    var previousCell
    var nextCell=output['nextCell']
    for(let i = 0; i <output['previousCell'].length; i++) {
        let cell = output['previousCell'][i]
        let index = mapCellToIndex(cell)

        if (board[index[0]][index[1]] != '--') {
            previousCell = cell
            output.previousCell = cell
            Playground.moveFigure(previousCell, nextCell);
            break
        }
    }
    captureCell(piece, previousCell, nextCell)
    Playground.moveFigure(previousCell, nextCell);

    return
}

// when there is more than one possibility move from the appropriate  piece which is saved on a location
const makeMoveFromSavedLocation = function(color, output, board) {
    let piece=color+output['piece']
    let nextCell=output['nextCell']

    let previousCell=findSavedCellLocation(piece)
    if (previousCell.length == 1) {
        previousCell = previousCell[0]
    } else {
        previousCell = getPreviousCellByPieceMove(piece, previousCell, nextCell)
    }

    output.previousCell = previousCell
    captureCell(piece, previousCell, nextCell)
    Playground.moveFigure(previousCell, nextCell);


    return
}

// helper function for makeMoveFromSavedLocation
const getPreviousCellByPieceMove = function(piece, previousCell, nextCell) {
    let numOfPieces = previousCell.length
    var previousCell
    for(let i = 0; i < numOfPieces; i++) {
        let capture = canCapture(piece[1], previousCell[i], nextCell)
        if(capture) {
            previousCell = previousCell[i]
            break
        }
    }
    return previousCell
}

// return true if type of a piece can capture the cell from a prev. cell
const canCapture = function(piece, previousCell, nextCell) {
    var sameRow, sameCol, sameDiagonal
    if(piece == 'R') {
        sameRow = checkOnSameRow(previousCell, nextCell)
        sameCol = checkOnSameCol(previousCell, nextCell)
    
        if(sameRow) {
            if(!checkPieceInRow(previousCell, nextCell)) {
                return true
            }
            return false
        } else if(sameCol) {
            if(!checkPieceInCol(previousCell, nextCell)) {
                return true
            }
            return false
        } else {
            return false
        }
    } else if(piece=='Q') {
        // if has on same diagonal or same row or same col
        sameDiagonal = checkOnSameDiagonal(previousCell, nextCell)
        sameRow = checkOnSameRow(previousCell, nextCell)
        sameCol = checkOnSameCol(previousCell, nextCell)
    
        if(sameRow) {
            if(!checkPieceInRow(previousCell, nextCell)) {
                return true
            }
            return false
        } else if(sameCol) {
            if(!checkPieceInCol(previousCell, nextCell)) {
                return true
            }
            return false
        } else if(sameDiagonal) {
            if(checkPieceInDiagonal(previousCell, nextCell)) {
                return true
            }
            return false
        } else {
            return false
        }
    } else if(piece == 'N') {
        let prevCellCol = map[previousCell[0]]
        let prevCellRow = parseInt(previousCell[1])
    
        let nextCellCol = map[nextCell[0]]
        let nextCellRow = parseInt(nextCell[1])
    
        let colDiff = Math.abs(prevCellCol - nextCellCol)
        let rowDiff = Math.abs(prevCellRow - nextCellRow)
    
        if((colDiff == 1 && rowDiff == 2) || (colDiff == 2 && rowDiff == 1)) {
            return true
        }
        return false
    } else if(piece == 'B') {
        let prevColor = getCellColor(previousCell)
        let nextColor = getCellColor(nextCell)
        if(prevColor == nextColor) {
            return true
        }
        return false
    }
}

// make move when there is only one possible piece to move there
const makeMoveByGivenLocation = function(color, output, board) {
    let piece=color+output['piece']
    let previousCell=output['previousCell']
    let nextCell=output['nextCell']
    captureCell(piece, previousCell, nextCell)
    Playground.moveFigure(previousCell, nextCell);

    return
}

// promote a cell by given type
const promote = function(cell, color, promotionType) {
    // let index = mapCellToIndex(cell)
    let piece = color+promotionType
    fillCell(cell, piece)

    return
}