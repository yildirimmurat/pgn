
// window.figure = (function() {
// 	const Figure = (name, color) => {
// 		this.name = name;
// 		this.color = color;
// 	}

// 	const figures =  {
// 		KING: 'king',
// 		QUEEEN: 'queen',
// 		ROOK: 'rook',
// 		BISHOP: 'bishop',
// 		KNIGHT: 'knight',
// 		PAWN: 'pawn',
// 	}

// 	return {
// 		Figure,
// 		figures
// 	}
// })();

// const kingw = window.figure.Figure(window.figure.figures.KING, 'white');
// const kingb = new Figure(figures.KING, white);
// const queenw = new Figure(figures.QUEEN, white);
// const queenb = new Figure(figures.QUEEN, white);
// const rookwl = new Figure(figures.ROOK, white);
// const rookwr = new Figure(figures.ROOK, white);
// const rookbl = new Figure(figures.ROOK, white);
// const rookbr = new Figure(figures.ROOK, white);
// const bishopwl = new Figure(figures.BISHOP, white);
// const bishopwr = new Figure(figures.BISHOP, white);
// const bishopbl = new Figure(figures.BISHOP, white);
// const bishopbr = new Figure(figures.BISHOP, white);
// const knightwl = new Figure(figures.KNIGHT, white);
// const knightwr = new Figure(figures.KNIGHT, white);
// const knightbl = new Figure(figures.KNIGHT, white);
// const knightbr = new Figure(figures.KNIGHT, white);
// const pawnb1 = new Figure(figures.PAWN, black);
// const pawnb2 = new Figure(figures.PAWN, black);
// const pawnb3 = new Figure(figures.PAWN, black);
// const pawnb4 = new Figure(figures.PAWN, black);
// const pawnb5 = new Figure(figures.PAWN, black);
// const pawnb6 = new Figure(figures.PAWN, black);
// const pawnb7 = new Figure(figures.PAWN, black);
// const pawnb8 = new Figure(figures.PAWN, black);
// const pawnw1 = new Figure(figures.PAWN, white);
// const pawnw2 = new Figure(figures.PAWN, white);
// const pawnw3 = new Figure(figures.PAWN, white);
// const pawnw4 = new Figure(figures.PAWN, white);
// const pawnw5 = new Figure(figures.PAWN, white);
// const pawnw6 = new Figure(figures.PAWN, white);
// const pawnw7 = new Figure(figures.PAWN, white);
// const pawnw8 = new Figure(figures.PAWN, white);

class Figure {
	constructor(name, color) {
		this.name = name;
		this.color = color;
	}
	get fig_name() {
		return this.name;
	}
	get fig_color() {
		return this.color;
	}
}

export default Figure;