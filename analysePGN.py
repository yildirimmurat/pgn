#!/usr/bin/python3
import sys
import re
import cs50

directory = "players/"
files = []

game = []
pgn = ""
flag = False

def main():
    # Reads the first argument if it exists 
    if (sys.argv.__len__()>1):
        file = sys.argv[1]

    open(f"pgn-database.db", "w").close()
    db = cs50.SQL("sqlite:///pgn-database.db")
    db.execute("CREATE TABLE games (GameID INTEGER PRIMARY KEY AUTOINCREMENT, Event TEXT, Site TEXT, Date TEXT, Round TEXT, White TEXT, Black TEXT, Result TEXT, WhiteElo INT, BlackElo INT , ECO TEXT, PGN TEXT)")

    with open(file, "r") as source:
        for line in source:
            files.append(line.strip())
    
    print("files: ", files)

    for i in range(len(files)):
        global flag
        flag = False
        with open(directory+files[i]+".pgn","r") as dataFile:
            print(directory+files[i]+".pgn")
            
            global game
            while(not flag):
                readMetaData(dataFile)
                # one empyt line
                dataFile.readline()
                #then read the game pgn
                readGamePGN(dataFile)

                # clear data first
                
                if(game[7]):
                    game[7] = int(game[7])
                else: 
                    game[7] = 0
                if(game[8]):
                    game[8] = int(game[8])
                else: 
                    game[8] = 0
                # insert datas to db
                db.execute("INSERT INTO games (Event, Site, Date, Round, White, Black, Result, WhiteElo, BlackElo , ECO, PGN) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", game[0], game[1], game[2], game[3], game[4], game[5], game[6], game[7], game[8], game[9], game[10])

                game = []
            # show all the games
            #print(db.execute("SELECT * FROM games"))






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
        global flag
        pgn = pgn + line.strip()
        endOfGame = re.search('(1-0|1/2-1/2|0-1)$', line) # TODO change it to just one option, it is on metadata
        if endOfGame:
            game.append(pgn)
            pgn = ''
            # read the empty line before going to next game
            if(not dataFile.readline()):
                flag = True
            break

main()