#!/usr/bin/python3
import sys
import re
import cs50

mainDatabase="pgn-database.db"
tableName="games"
columnName="PGN"
# TODO parametric
selectedRow=50000

games={}
moves={}

moveNumber = 1





def main():
    games = getGamesFromDatabase()
    for i in range(selectedRow):
        print("reading game ", i+1)
        insertMovesFromGame(i+1, games)


def getGamesFromDatabase():
    global games

    with open(f''+mainDatabase, "r"):
        db = cs50.SQL("sqlite:///"+mainDatabase)
        games = db.execute("SELECT "+columnName+" FROM "+tableName)
    
    return games

def insertMovesFromGame(selectedRow, games):
    global moveNumber
    game=games[selectedRow - 1][columnName]
    gameMoves=game.split(" ")
    
    # create moves table
    #with open(f"pgn-database.db", "a"):
    moveDB = cs50.SQL("sqlite:///pgn-database.db")
        #moveDB.execute("CREATE TABLE moves (game_id, moveID INTEGER PRIMARY KEY AUTOINCREMENT, moveNumber INT, color TEXT, move TEXT, FOREIGN KEY(game_id) REFERENCES games(GameID))")
    
    for i in range(len(gameMoves)):
        regex="\d{1,}\.(.*)"
        match=re.search(regex, gameMoves[i])
        if match:
            # print("White move on moveNum ",moveNumber,": ", match.group(1))
            moveDB.execute("INSERT INTO moves (game_id, moveNumber, color, move) VALUES(?, ?, ?, ?)", selectedRow, moveNumber, "White", match.group(1))
        else:
            if(gameMoves[i] == ""):
                # game is finished
                # print("Result: ", gameMoves[i+1])
                break
            # print("Black move on moveNum ",moveNumber,": ", gameMoves[i])
            moveDB.execute("INSERT INTO moves (game_id, moveNumber, color, move) VALUES(?, ?, ?, ?)", selectedRow, moveNumber, "Black", gameMoves[i])

            moveNumber += 1


main()