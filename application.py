from flask import Flask, render_template
from createSimpleGame import readMovesFromGame, readMetaDataFromGame
import random
app = Flask(__name__)


@app.route('/')
def index():
    # TO DO
    # make range parametric
    gameId=random.randint(1, 100)
    moveList = readMovesFromGame(gameId)

    # TO DO
    # all metadata into an array
    event = readMetaDataFromGame(gameId, 'Event')[0]['Event']
    site = readMetaDataFromGame(gameId, 'Site')[0]['Site']
    date = readMetaDataFromGame(gameId, 'Date')[0]['Date']
    _round = readMetaDataFromGame(gameId, 'Round')[0]['Round']
    white = readMetaDataFromGame(gameId, 'White')[0]['White']
    black = readMetaDataFromGame(gameId, 'Black')[0]['Black']
    result = readMetaDataFromGame(gameId, 'Result')[0]['Result']
    whiteElo = readMetaDataFromGame(gameId, 'WhiteElo')[0]['WhiteElo']
    blackElo = readMetaDataFromGame(gameId, 'BlackElo')[0]['BlackElo']
    ECO = readMetaDataFromGame(gameId, 'ECO')[0]['ECO']
    return render_template('index.html', gameId=gameId, moveList=moveList, event= event, site=site, date=date, _round=_round, white=white, black=black, result=result, whiteElo=whiteElo, blackElo=blackElo, ECO=ECO)