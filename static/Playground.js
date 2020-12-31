import Figure from './Figure.js';
export default class Playground {

	
	
	static printMatrix() {
		//create 8by8 matrix
		let flip = false;////
		let $board = $('.board');
		for(let i = 0; i < 8; i++) {
			for(let j = 0; j < 8; j++) {
				let $cell = $(document.createElement('div'));
				$cell.addClass('cell');
				$cell.addClass(`cell-${this.changeColLabel(flip, j)}${this.changeRowLabel(flip, i)}`);
				$cell.addClass(`cell-${this.getColor(flip, i, j)}`);
				$board.append($cell);
			}
		}
	}

	static putPiece(piece, cell) {
		let p = piece.fig_color + '_' + piece.fig_name;
		let $board = $('.board');
		cell.forEach((c) => {
			let $cellElement = $board.find('.cell-' + c);
			$cellElement.append(`<img src = '/static/images/${p}.png' alt='piece'>`);
		})
	}

	static putPieces(piecesWithCells) {
		piecesWithCells.forEach ((element) => {
			let piece = element.piece;
			let cell = element.cell;
			this.putPiece(piece, cell);
		})
	}

	static startUpPieces(flip) {
		if(!flip) {
			Playground.putPieces([
				{piece: rookw, cell: ['a1', 'h1']},
				{piece: knightw, cell: ['b1', 'g1']},
				{piece: bishopw, cell: ['c1', 'f1']},
				{piece: queenw, cell: ['d1']},
				{piece: kingw, cell: ['e1']},
				{piece: pawnw, cell: ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']},

				{piece: rookb, cell: ['a8', 'h8']},
				{piece: knightb, cell: ['b8', 'g8']},
				{piece: bishopb, cell: ['c8', 'f8']},
				{piece: queenb, cell: ['d8']},
				{piece: kingb, cell: ['e8']},
				{piece: pawnb, cell: ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7']}]);
		}
	}

	static moveFigure(cell1, cell2) {
		let $board = $('.board');
		let figureToMove = $board.find('.cell-' + cell1).find('img').detach();
		let $cellToMove = $board.find('.cell-' + cell2);
		$cellToMove.append(figureToMove);
	}

	static removeFigure(cell) {
		let $board = $('.board');
		$board.find('.cell-' + cell).find('img').remove();
	}
	
	static highlightMove(prev, next) {
		let board = $('.board');
		let fromCell = $(board).find('.from')
		let toCell = $(board).find('.to')
		$(fromCell).removeClass('from')
		$(toCell).removeClass('to')

		let prevCell = $(board).find('.cell-' + prev)
		let nextCell = $(board).find('.cell-' + next)

		$(prevCell).addClass('from')
		$(nextCell).addClass('to')

	}

	static changeColLabel(flip, label) {
		if(!flip) {
			switch(label) {
				case 0:
					return 'a';
				case 1:
					return 'b';
				case 2:
					return 'c';
				case 3:
					return 'd';
				case 4:
					return 'e';
				case 5:
					return 'f';
				case 6:
					return 'g';
				case 7:
					return 'h';
				default:
					break;
			}
		}
	}

	static changeRowLabel(flip, label) {
		if(!flip) {
			return 8 - label;
		}
	}

	static getColor(flip, i, j) {
		if(!flip) {
			if((i+j) % 2 == 0)
				return 'white';
			else
				return 'dark';
		}
	}



	static startGame() {
		return "startGame has been called.";
	}

	// static addFigures() {
	// 	return "addFigures has been called.";
	// }

	// static clickMove() {
	// 	return "clickMove has been called.";
	// }

	// static moveFigure() {
	// 	return "moveFigure has been called.";
	// }
}

let $board = $('.board').find('.cell');
$board.on('click', function() {
	console.log('cell clicked.');
});

Playground.printMatrix();


const rookw = new Figure('rook', 'white');
const knightw = new Figure('knight', 'white');
const bishopw = new Figure('bishop', 'white');
const queenw = new Figure('queen', 'white');
const kingw = new Figure('king', 'white');
const pawnw = new Figure('pawn', 'white');

const rookb = new Figure('rook', 'black');
const knightb = new Figure('knight', 'black');
const bishopb = new Figure('bishop', 'black');
const queenb = new Figure('queen', 'black');
const kingb = new Figure('king', 'black');
const pawnb = new Figure('pawn', 'black');




Playground.startUpPieces(false);

// sleep(1000)
// Playground.moveFigure('e2', 'e4');
// sleep(1000)
// Playground.moveFigure('c7', 'c6');
// sleep(1000)
// Playground.moveFigure('d2', 'd4');
// sleep(1000)
// Playground.moveFigure('d7', 'd5');
// sleep(1000)
// Playground.moveFigure('e4', 'd5');

