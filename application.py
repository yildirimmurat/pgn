from flask import Flask, render_template
from createSimpleGame import readMovesFromGame
import random
app = Flask(__name__)


@app.route('/')
def index():
    # TO DO
    # make range parametric
    gameId=random.randint(1, 9709)
    moveList = readMovesFromGame(gameId)
    print(moveList)
    return render_template('index.html', moveList=moveList)