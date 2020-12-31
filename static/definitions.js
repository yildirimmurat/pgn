// 2D board array
const ROWS = 8
const COLS = 8
window.board = new Array(ROWS)
for (let i = 0; i < ROWS; i++) {
    board[i] = new Array(COLS)
    for (let j = 0; j < COLS; j++) {
        board[i][j] = '--'
    }
}

window.colors = {
    'WHITE' : 'W',
    'BLACK': 'B'
}

window.map={
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7
}

window.savedLocations = {}

// helper function
window.mapCellToIndex = function(location) {
    let desiredCol = location.slice(0,1)
    let desiredRow = location.slice(1)

    let indexRow = parseInt(desiredRow) - 1
    let indexCol = map[desiredCol]

    return [indexRow, indexCol]
}

// helper function
window.mapIndexToCell = function(index) {
    let map=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    let row=index[0]+1
    let col=map[index[1]]

    return col+row.toString()
}

window.switchColor = function(color) {
    if(color == colors['WHITE']) {
        return colors['BLACK']
    } else{
        return colors['WHITE']
    }
}

window.emptyCell = function(previousCell) {
    console.log('in empty cell')
    console.log('previousCell: ' + previousCell)
    let previousIndex = mapCellToIndex(previousCell)
    console.log('previousIndex: ' + previousIndex)
    let piece=board[previousIndex[0]][previousIndex[1]]

    let a = [previousCell]
    console.log('a: '+a)
    let b = savedLocations[piece]
    console.log('b;'+b)
    let diff = arr_diff(a, b)
    console.log('diff: ' + diff)
    savedLocations[piece] = diff

    board[previousIndex[0]][previousIndex[1]] = '--'

    return
}

// fill cell with a given piece
window.fillCell = function(nextCell, piece){
    let nextIndex = mapCellToIndex(nextCell)
    board[nextIndex[0]][nextIndex[1]] = piece

    savedLocations[piece].push(nextCell)

    return
}

// https://stackoverflow.com/questions/1187518/how-to-get-the-difference-between-two-arrays-in-javascript
function arr_diff (a1, a2) {

    var a = [], diff = [];

    for (var i = 0; i < a1.length; i++) {
        a[a1[i]] = true;
    }

    for (var i = 0; i < a2.length; i++) {
        if (a[a2[i]]) {
            delete a[a2[i]];
        } else {
            a[a2[i]] = true;
        }
    }

    for (var k in a) {
        diff.push(k);
    }

    return diff;
}

// return saved locations of the given piece
window.findSavedCellLocation = function(piece) {
    return savedLocations[piece]
}

// returns True if two given cells are on same row
window.checkOnSameRow = function(previousCell, nextCell) {
    if(previousCell[1] == nextCell[1]) {
        return true
    }
    return false
}

// returns True if two given cells are on same column
window.checkOnSameCol = function(previousCell, nextCell) {
    if(previousCell[0] == nextCell[0]) {
        return true
    }
    return false
}

// returns True if two given cells are on same diagonal
window.checkOnSameDiagonal = function(previousCell, nextCell) {
    let prevCellCol = map[previousCell[0]]
    let prevCellRow = parseInt(previousCell[1])
    let prevCellDiff = prevCellCol - prevCellRow
    
    let nextCellCol = map[nextCell[0]]
    let nextCellRow = parseInt(nextCell[1])
    let nextCellDiff = nextCellCol - nextCellRow
    
    if(prevCellDiff == nextCellDiff) {
        return true
    }
    return false
}

// returns False if there is no piece between cells which are on same row
window.checkPieceInRow = function(previousCell, nextCell) {
    var row = parseInt(previousCell[1]) - 1
    
    let prevCol = map[previousCell[0]]
    let nextCol = map[nextCell[0]]
    
    if(prevCol > nextCol) {
        // https://stackoverflow.com/questions/16201656/how-to-swap-two-variables-in-javascript
        nextCol = [prevCol, prevCol = nextCol][0];
    }
    
    // CHECK IF adjacent cells
    if(nextCol - prevCol == 1) {
        return false
    } else {
        for(let i = prevCol + 1; i < nextCol; i++) {
            let searchIndex = [row, i]
            let cell = mapIndexToCell(searchIndex)
            let val = getCellValue(board, cell)
            if(val != '--') {
                return true
            }
        }
        return false
    }
}

// return the piece that is on the cell
window.getCellValue = function(board, cell) {
    let index = mapCellToIndex(cell)
    return board[index[0]][index[1]]
}

// returns False if there is no piece between cells which are on same col
window.checkPieceInCol = function(previousCell, nextCell) {
    let col = map[previousCell[0]]
    
    let prevRow = parseInt(previousCell[1]) - 1
    let nextRow = parseInt(nextCell[1]) - 1
    
    if(prevRow > nextRow) {
        // https://stackoverflow.com/questions/16201656/how-to-swap-two-variables-in-javascript
        nextRow = [prevRow, prevRow = nextRow][0];
    }
    
    // CHECK IF adjacent cells
    if(nextRow - prevRow == 1) {
        return false
    } else {
        for(let i = prevRow + 1; i < nextRow; i++) {
            let searchIndex = [i, col]
            let cell = mapIndexToCell(searchIndex)
            let val = getCellValue(board, cell)
            if(val != '--') {
                return true
            }
        }
        return false 
    }
}
    
// returns False if there is no piece between cells which are on same diagonal
window.checkPieceInDiagonal = function(previousCell, nextCell) {
    var prevRow = parseInt(previousCell[1]) - 1
    var nextRow = parseInt(nextCell[1]) - 1
    
    var prevCol = map[previousCell[0]]
    var nextCol = map[nextCell[0]]
    
    var toUp = 1
    if(prevRow > nextRow) {
        // https://stackoverflow.com/questions/16201656/how-to-swap-two-variables-in-javascript
        nextCol = [prevCol, prevCol = nextCol][0];
        nextRow = [prevRow, prevRow = nextRow][0];
    }
    if(prevCol > nextCol) {
        // if previous cell is on the upper part of the board, then go downwards while searching
        toUp = -1
    }
    
    // CHECK IF adjacent cells
    if(nextRow - prevRow == 1) {
        return false
    } else {
        let col = prevCol
        for(let i = prevRow + 1; i < nextRow; i ++) {
            col = col + toUp
            let searchIndex = [i, col]
            let cell = mapIndexToCell(searchIndex)
            let val = getCellValue(board, cell)
            if(val != '--') {
                return true
            }
        }
        return false
    }
}

// return the color of cell
window.getCellColor = function(cell) {
    let index=mapCellToIndex(cell)
    if((index[0]+index[1]) % 2 == 0) {
        return colors['WHITE']
    } else {
        return colors['BLACK']
    }
}
    