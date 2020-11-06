#!/usr/bin/python3
import sys
import re
import cs50

# definitions
mainDatabase="pgn-database.db"
tableName="moves"
columnName="move"
idColumn="moveID"
# TODO parametric
selectedRow=52

# Output variables
isCheck=False
takes=False
previousCell=""
nextCell=""
piece=""

pieces={
    'K': "King",
    'Q': "Queen",
    'R': "Rook",
    'N': "Knight",
    'B': "Bishop"
}

def main():
    global isCheck
    global takes
    global piece
    global previousCell
    global nextCell

    # read a single move from database
    with open(f''+mainDatabase, "r"):
        db = cs50.SQL("sqlite:///"+mainDatabase)
        # move = db.execute("SELECT "+columnName+" FROM "+tableName+" WHERE "+idColumn+"="+str(selectedRow))[0]['move']

    for i in range(150):# TODO not hardcoded here
        isCheck=False
        takes=False
        move = db.execute("SELECT "+columnName+" FROM "+tableName+" WHERE "+idColumn+"="+str(i+1))[0]['move']

        # print input
        print("==========")
        print("move: "+move)
        print("...........")

        #check if it is a check
        if(move[len(move)-1] == "+"):
            move=move[:len(move)-1]
            isCheck=True
            # print("Check")


        if(move=="O-O"):
            piece="Castle short"
        elif(move=="O-O-O"):
            piece="Castle long"
        elif(len(move)==2):
            nextCell=move
            if(move[1] == "4"):
                previousCell=move[0]+"3 or "+move [0]+"2"
            else:
                previousCell=move[0]+str((int(move[1])-1))
        else:
            # print("not pawn")
            if(len(move) == 4 and move[1] == "x"):
                takes=True
                try:
                    piece=pieces[move[0]]
                    previousCell="saved location of the piece"
                    nextCell=move[2:]
                except:
                    piece="Pawn"
                    previousCell=move[0]+str((int(move[3])-1))
                    nextCell=move[2:]

                move=move[2:]
            else:
                if(len(move) == 4):
                    # TODO
                    print("!!!!!!!!!!!!!!")
                    print("4 letters without x???")
                    print("!!!!!!!!!!!!!!")
                elif(len(move)==3):
                    # a piece move to a empty cell
                    piece=pieces[move[0]]
                    previousCell="saved location of the piece"
                    nextCell=move[1:]
                else:
                    # TODO
                    print("????!!!??")
                    print("!!!!!????!!!")



        print("isCheck: ",isCheck)
        print("takes: ", takes)
        print("previousCell: ", previousCell)
        print("nextCell: ", nextCell)
        print("piece:", piece)
        print("============")

























main()