// put pieces into default location in the beginning of the game
"use strict"

window.initializeBoard = function() {
    // default position
    // first letter is whether it is (W)hite or (B)lack
    // second letter is about type of piece (Q):Queen etc.    putPieceIntoBoard('BR', 'a8')
    putPieceIntoBoardByArray([['BR', 'a8'], ['BN', 'b8'], ['BB', 'c8'], ['BQ', 'd8'], ['BK', 'e8'], ['BB', 'f8'], ['BN', 'g8'], ['BR', 'h8']])
    putPieceIntoBoardByArray([['Bp', 'a7'], ['Bp', 'b7'], ['Bp', 'c7'], ['Bp', 'd7'], ['Bp', 'e7'], ['Bp', 'f7'], ['Bp', 'g7'], ['Bp', 'h7']])
    putPieceIntoBoardByArray([['Wp', 'a2'], ['Wp', 'b2'], ['Wp', 'c2'], ['Wp', 'd2'], ['Wp', 'e2'], ['Wp', 'f2'], ['Wp', 'g2'], ['Wp', 'h2']])
    putPieceIntoBoardByArray([['WR', 'a1'], ['WN', 'b1'], ['WB', 'c1'], ['WQ', 'd1'], ['WK', 'e1'], ['WB', 'f1'], ['WN', 'g1'], ['WR', 'h1']])
    
    savedLocations['BR']=['a8', 'h8']
    savedLocations['BN']=['b8', 'g8']
    savedLocations['BB']=['c8', 'f8']
    savedLocations['BQ']=['d8'] // saved as an array because afterwards pawns could promote
    savedLocations['BK']=['e8']
    savedLocations['Bp']=['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7']

    savedLocations['WR']=['a1', 'h1']
    savedLocations['WN']=['b1', 'g1']
    savedLocations['WB']=['c1', 'f1']
    savedLocations['WQ']=['d1'] // saved as an array because afterwards pawns could promote
    savedLocations['WK']=['e1']
    savedLocations['Wp']=['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']

    return
}

// puts multiple pieces into board
const putPieceIntoBoardByArray = function(arr) {
    for(let i = 0; i < arr.length; i++) {
        let piece=arr[i][0]
        let location=arr[i][1]
        putPieceIntoBoard(piece, location)
    }
    return
}

// puts a piece into a desired location on the board
const putPieceIntoBoard = function(piece, location) {
    let index=mapCellToIndex(location)
    let row=index[0]
    let col=index[1]
    board[row][col] = piece

    return  
}