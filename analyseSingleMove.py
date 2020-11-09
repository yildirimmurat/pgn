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


pieces={
    'K': "King",
    'Q': "Queen",
    'R': "Rook",
    'N': "Knight",
    'B': "Bishop",
    'p': "Pawn"
}

def main():

    # read a single move from database
    with open(f''+mainDatabase, "r"):
        db = cs50.SQL("sqlite:///"+mainDatabase)
        # move = db.execute("SELECT "+columnName+" FROM "+tableName+" WHERE "+idColumn+"="+str(selectedRow))[0]['move']

    for i in range(2):# TODO not hardcoded here
        print("analysing move",i+1)
        move = db.execute("SELECT "+columnName+" FROM "+tableName+" WHERE "+idColumn+"="+str(i+1))[0]['move']

        # print input
        print("==========")
        print("move: "+move)
        print("...........")

        output = makeMove(move)

        # print output
        print("isCheck: ", output['isCheck'])
        print("takes: ", output['takes'])
        print("previousCell: ", output['previousCell'])
        print("nextCell: ", output['nextCell'])
        print("piece:", output['piece'])
        print("============")


        


def makeMove(move, color='W', isCheck=False, takes=False):

    # TODO
    # add moves like c8=Q, d8=Q+
    # bxc1=Q. dxc8=N+
    # create sub functions
    # check if-else logic

    output={}

    output['isCheck']=isCheck
    output['takes']=takes


    #check if it is a check
    if(move[len(move)-1] == "+"):
        move=move[:len(move)-1]
        output['isCheck']=True

    if(move=="O-O"):
        output=castleShort(output, color)

    elif(move=="O-O-O"):
        output=castleLong(output, color)

    elif(len(move)==2):
        # e.g e4
        output=pawnForward(output, move, color)

    else:
        # e.g Qxb5
        if(len(move) == 4 and move[1] == "x"):
            print('in piece takes fun')
            output=pieceTakes(output, move, color)

        else:
            # e.g Nbd3
            if(len(move) == 4):
                # TODO
                print("!!!!!!!!!!!!!!")
                print("4 letters without x???")
                print("!!!!!!!!!!!!!!")
                try:
                    output['piece']=move[0]
                except:
                    # e.g a1=Q
                    output['piece']="exception move"
                output['previousCell']='saved location of row or col:'+move[1]
                output['nextCell']=move[2:]

            elif(len(move)==3):
                # a piece move to a empty cell
                output['piece']=move[0]
                output['previousCell']="saved location of the piece"
                output['nextCell']=move[1:]
            else:
                # TODO
                print("????!!!??")
                print("!!!!!????!!!")
                try:
                    output['piece']=move[0]
                except:
                    output['piece']="exception piece"
                output['previousCell']="saved location of row or col:"+move[1]
                output['nextCell']=move[3:]
                output['takes']=True

    return output


def castleShort(output, color):
    output['piece']=['K', 'R']

    if color=="W":
        # white castle short
        output['previousCell']=['e1', 'h1']
        output['nextCell']=['g1', 'f1']
    else:
        # black castle short
        output['previousCell']=['e8', 'h8']
        output['nextCell']=['g8', 'f8']

    return output

def castleLong(output, color):
    output['piece']=['K', 'R']

    if color=="W":
        # white castle long
        output['previousCell']=['e1', 'a1']
        output['nextCell']=['c1', 'd1']
    else:
        # black castle long
        output['previousCell']=['e8', 'a8']
        output['nextCell']=['c8', 'd8']

    return output

def pawnForward(output, move, color):
    output['nextCell']=move
    output['piece']='p'
    if (move[1] == "4" and color == 'W'):
        output['previousCell']=[move[0]+"3", move [0]+"2"]
    elif (move[1] == "5" and color == 'B'):
        output['previousCell']=[move[0]+"6", move [0]+"7"]
    elif (color == 'W'):
        output['previousCell']=move[0]+str((int(move[1])-1))
    else:
        # black
        output['previousCell']=move[0]+str((int(move[1])+1))

    return output

def pieceTakes(output, move, color):
    output['takes']=True

    if (move[0].isupper()):
        # e.g Qxb3
        output['piece']=move[0]
        output['previousCell']="previousCell"
        output['nextCell']=move[2:]
    else:
        # e.g axb8
        output['piece']='p'
        if color == 'W':
            output['previousCell']=move[0]+str((int(move[3])-1))
        else:
            output['previousCell']=move[0]+str((int(move[3])+1))
            
        output['nextCell']=move[2:]

    return output


main()

























main()