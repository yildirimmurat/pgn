// import {Figure, figures} from './js/src/Figure.js';
//$(".board").hide();//doesn't work as expected


// $(document).ready(function() {
//     $(".board").hide(1000);
// });

// $(function() {
//     $('.board').hide(1000);
// });

// $(function() {
//     $('.cell').on('click', function() {
//         $(this).find('img').hide(1000);
//     })
// });

$(function() {
    // const startPosition = () => {
    //     const cellArray = $('.cell');
    //     cellArray.each(function(index) {
    //         $(this).find("img").remove();
    //         $(this).append("<img src=\"./images/black_rook.png\"></img>");
    //     });
    // }

    // startPosition();
    class Figure {
        constructor(name, color) {
            this.name = name;
            this.color = color;
        }
        getName() {
            return this.name;
        }
        getColor() {
            return this.color;
        }
    }

	const figures =  {
		KING: 'king',
		QUEEN: 'queen',
		ROOK: 'rook',
		BISHOP: 'bishop',
		KNIGHT: 'knight',
		PAWN: 'pawn',
    }
    
    const kingw = new Figure(figures.KING, 'white');
    const kingb = new Figure(figures.KING, 'black');
    const queenw = new Figure(figures.QUEEN, 'white');
    const queenb = new Figure(figures.QUEEN, 'black');
    const rookw = new Figure(figures.ROOK, 'white');
    const rookb = new Figure(figures.ROOK, 'black');
    const bishopw = new Figure(figures.BISHOP, 'white');
    const bishopb = new Figure(figures.BISHOP, 'black');
    const knightw = new Figure(figures.KNIGHT, 'white');
    const knightb = new Figure(figures.KNIGHT, 'black');
    const pawnb = new Figure(figures.PAWN, 'black');
    const pawnw = new Figure(figures.PAWN, 'white');

 
    // const putPiece = (Figure, id) => {
    //     let cellId = `#${id}`;
    //     let pieceName = Figure.getName();
    //     let pieceColor = Figure.getColor();
    //     $(cellId).append("<img src=\"./images/" + pieceColor + "_" + pieceName + ".png\"></img>");
    // }

    const putPieces = arr => {
        for(let i = 0; i < arr.length; i++) {
            let fig = arr[i].Figure;
            let id = arr[i].id;

            let cellId = `#${id}`;
            let pieceName = fig.getName();
            let pieceColor = fig.getColor();
            $(cellId).append("<img src=\"./images/" + pieceColor + "_" + pieceName + ".png\"></img>");

        }
    }

    // let myArr = [
    //     {Figure: kingw, id: '11'},
    //     {Figure: kingb, id: '12'}
    // ]

    let startingPositionArray = [
        {Figure: rookb, id: '11'},
        {Figure: knightb, id: '12'},
        {Figure: bishopb, id: '13'},
        {Figure: queenb, id: '14'},
        {Figure: kingb, id: '15'},
        {Figure: bishopb, id: '16'},
        {Figure: knightb, id: '17'},
        {Figure: rookb, id: '18'},

        {Figure: pawnb, id: '21'},
        {Figure: pawnb, id: '22'},
        {Figure: pawnb, id: '23'},
        {Figure: pawnb, id: '24'},
        {Figure: pawnb, id: '25'},
        {Figure: pawnb, id: '26'},
        {Figure: pawnb, id: '27'},
        {Figure: pawnb, id: '28'},

        {Figure: pawnw, id: '71'},
        {Figure: pawnw, id: '72'},
        {Figure: pawnw, id: '73'},
        {Figure: pawnw, id: '74'},
        {Figure: pawnw, id: '75'},
        {Figure: pawnw, id: '76'},
        {Figure: pawnw, id: '77'},
        {Figure: pawnw, id: '78'},

        {Figure: rookw, id: '81'},
        {Figure: knightw, id: '82'},
        {Figure: bishopw, id: '83'},
        {Figure: queenw, id: '84'},
        {Figure: kingw, id: '85'},
        {Figure: bishopw, id: '86'},
        {Figure: knightw, id: '87'},
        {Figure: rookw, id: '88'},
    ]

    // putPiece(kingw, '11');
    putPieces(startingPositionArray);

    $('.cell').on('click', function() {
        //define its starting position
        //when clicked in another square
            //detach the figure from old place
            //and put in the new place
        let cellId1 = $(this).attr('id');
        while(true) {
            $('.cell').on('click', function() {
                let cellId2 = $(this).attr('id');
                if(cellId1 !== cellId2) {
                    let fig = $('this').find('img').detach();
                    
                }
            })
        }

        return false;
    });
})