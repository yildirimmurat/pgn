window.sleep = (ms) => {
    var start = new Date().getTime(), expire = start + ms;
    while (new Date().getTime() < expire) { }
    return;
}


window.moveFigure = (cell1, cell2) => {
    let $board = $('.board');
    let figureToMove = $board.find('.cell-' + cell1).find('img').detach();
    let $cellToMove = $board.find('.cell-' + cell2);
    $cellToMove.append(figureToMove);
}