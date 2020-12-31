window.analyseMove = function(board, move, color, isCheck=false, takes=false, promotion='') {
    // TODO
    // bxc1=Q. dxc8=N+
    // check if-else logic

    var output={}
    output['isCheck']=isCheck
    output['takes']=takes
    output['promotion']=''

    // check if it is a check
    var lastLiteral = move[move.length - 1]
    if(lastLiteral == '+') {
        move = move.slice(0, -1)
        output['isCheck']=true
    }

    if(move == "O-O") {
        output=analyseCastleShort(output, color)
    } else if(move == "O-O-O") {
        output=analyseCastleLong(output, color)
    } else if(move.length == 2) {
        // e.g e4
        output=pawnForward(output, move, color)
    } else if(move.length == 3) {
        // a piece move to a empty cell, e.g Rb1, Bd7
        output = normalPieceMove(output, move)
    } else if(move.length == 4) {
        // e.g Qxb5
        if(move[1] == 'x') {
            output=pieceTakes(output, move, color)
        } else if(move[2] == '=') {
            // e.g a8=Q
            output = pawnPromote(board, move, color)
        } else {
            // e.g Nbd3
            output = moveByLocationHint(output, board, move, color)
        }
    } else if(move.length == 5) {
        // e.g Nbxd4
        if(move[2] != 'x') {
            console.log("????!!!??")
            console.log('MOVE: ', move)
            console.log("!!!!!????!!!")
        } else {
            move = move.replace('x', '')
            console.log(move)
            output = analyseMove(board, move, color=color)
            output['takes'] = true
        }
    } else {
        // e.g bxc1=Q
        if(move[move.length - 2] != '=') {
            console.log("????!!!??")
            console.log('MOVE: ', move)
            console.log("!!!!!????!!!")
        } else {
            let promoteTo = move[-1]
            move = move.slice(0, -2)
            console.log('move: '+move)
            output = analyseMove(board, move, color = color)
            output['promotion'] = promoteTo
        }
    }

    return output

}

// get outputs of short castling, O-O
const analyseCastleShort = function(output, color) {
    output['piece'] = ['K', 'R']

    if(color == colors['WHITE']) {
        // white castle short
        output['previousCell']=['e1', 'h1']
        output['nextCell']=['g1', 'f1']
    } else {
        // black castle short
        output['previousCell']=['e8', 'h8']
        output['nextCell']=['g8', 'f8']
    }

    return output
}

// get outputs of long castling, O-O-O
const analyseCastleLong = function(output, color) {
    output['piece']=['K', 'R']

    if(color == colors['WHITE']) {
        // white castle long
        output['previousCell']=['e1', 'a1']
        output['nextCell']=['c1', 'd1']
    } else {
        // black castle long
        output['previousCell']=['e8', 'a8']
        output['nextCell']=['c8', 'd8']
    }

    return output
}

// get output of forward pawn move like e4
const pawnForward = function(output, move, color) {
    output['nextCell']=move
    output['piece']='p'
    if(move[1] == "4" && color == colors['WHITE']) {
        output['previousCell']=[move[0]+"3", move[0]+"2"]
    } else if(move[1] == "5" && color == 'B') {
        output['previousCell']=[move[0]+"6", move [0]+"7"]
    } else if(color == 'W') {
        output['previousCell']=move[0]+((parseInt(move[1])-1).toString())
    } else {
        // black
        output['previousCell']=move[0]+(parseInt(move[1])+1).toString()
    }

    return output
}

// get output of normal piece move like Nb3
const normalPieceMove = function(output, move) {
    output['piece']=move[0]
    output['previousCell']="previousCell"
    output['nextCell']=move.slice(1)

    return output
}

// get output of piece takes move like Bxe3
const pieceTakes = function(output, move, color) {
    output['takes']=true

    if(move[0] == move[0].toUpperCase()) {
        // e.g Qxb3
        output['piece']=move[0]
        output['previousCell']="previousCell"
        output['nextCell']=move.slice(2)
    } else {
        // e.g axb7
        output['piece']='p'
        if(color == colors['WHITE']) {
            output['previousCell']=move[0]+(parseInt(move[3])-1).toString()
        } else {
            output['previousCell']=move[0]+(parseInt(move[3])+1).toString()
        }
            
        output['nextCell']=move.slice(2)
    }

    return output
}

// get output of pawn promotion move, a1=Q
const pawnPromote = function(board, move, color) {
    let promoteTo = move[3]
    move = move.slice(0,2)
    output = analyseMove(board, move, color=color)
    console.log(output)
    output['promotion'] = promoteTo

    return output
}

// get output of move by location hint like Nbd3
const moveByLocationHint = function(output, board, move, color) {
    output['piece'] = move[0]
    var locationHint = move[1]
    if(isNaN(parseInt(locationHint))) {
        // find the piece in col of locationHint
        output['previousCell'] = findCellByColLocation(board, color+output['piece'], locationHint)
    } else {
        // find the piece in row of locationHint
        output['previousCell'] = findCellByRowLocation(board, color+output['piece'], locationHint)
    }
    output['nextCell']=move.slice(2)

    return output
}

// return the cell containing a certain piece by searching an entire row
const findCellByRowLocation = function(board, piece, locationHint) {
    for(let i = 0; i < 8; i++) {
        let col = i
        let row = parseInt(locationHint) - 1

        var cell = mapIndexToCell([row, col])

        if(board[row][col] == piece) {
            return cell
        }
    }
    return false
}

// return the cell containing a certain piece by searching an entire col
const findCellByColLocation = function(board, piece, locationHint) {
    for(let i = 0; i < 8; i++) {
        let row = i
        let col= map[locationHint]

        var cell = mapIndexToCell([row, col])

        if(board[row][col] == piece) {
            return cell
        }
    }
    return false
}
