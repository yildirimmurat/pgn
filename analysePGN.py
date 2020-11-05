#!/usr/bin/python3
import sys
import re

countGames = 0
games = []
game = []
pgn = ""

countLineInGame = 0
event = []

def main():
    # Reads the first argument if it exists 
    if (sys.argv.__len__()>1):
        file = sys.argv[1]
 
    with open(file,"r") as dataFile:
        readMetaData(dataFile)
        # one empyt line
        dataFile.readline()
        #then read the game pgn
        readGamePGN(dataFile)
        print(game)


def readMetaData(dataFile):
    dataArr = ['Event', 'Site', 'Date', 'Round', 'White', 'Black', 'Result', 'WhiteElo', 'BlackElo', 'ECO']
    for i in range(10):
        lineToBeRead = dataFile.readline()
        dataToBeAppended = re.search(dataArr[i]+" \"(.*)\"", lineToBeRead)
        if dataToBeAppended:
            game.append(dataToBeAppended.group(1))
        else:
            game.append('')

def readGamePGN(dataFile):
    for line in dataFile:
        global pgn
        pgn = pgn + line.strip()
        endOfGame = re.search('(1-0|1/2-1/2|0-1)$', line) # TODO change it to just one option, it is on metadata
        if endOfGame:
            game.append(pgn)
            pgn = ''
            # read the empty line before going to next game
            dataFile.readline()
            break

main()