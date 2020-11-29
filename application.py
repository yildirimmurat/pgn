from flask import Flask, render_template
from createSimpleGame import readMovesFromGame
app = Flask(__name__)


@app.route('/')
def index():
    gameId=1
    moveList = readMovesFromGame(gameId)
    print(moveList)
    return render_template('index.html', moveList=moveList)