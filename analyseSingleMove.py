#!/usr/bin/python3
import sys
import re
import cs50
from helpers import *

# definitions
mainDatabase="pgn-database.db"
tableName="moves"
columnName="move"
idColumn="moveID"
# TODO parametric
selectedRow=52






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


        board = {}#TODO
        output = makeMove(board, move)

        # print output
        print("promotion: ", output['promotion'])
        print("isCheck: ", output['isCheck'])
        print("takes: ", output['takes'])
        print("previousCell: ", output['previousCell'])
        print("nextCell: ", output['nextCell'])
        print("piece:", output['piece'])
        print("============")


        


def makeMove(board, move, color='W', isCheck=False, takes=False, promotion=''):
    # TODO
    # bxc1=Q. dxc8=N+
    # check if-else logic

    output={}
    output['isCheck']=isCheck
    output['takes']=takes
    output['promotion']=''

    #check if it is a check
    lastLiteral = move[len(move) - 1]
    if lastLiteral == '+':
        move = move[:-1]
        output['isCheck']=True

    if move == "O-O":
        output=castleShort(output, color)

    elif move == "O-O-O":
        output=castleLong(output, color)

    elif len(move)==2:
        # e.g e4
        output=pawnForward(output, move, color)

    else:
        # e.g Qxb5
        if(len(move) == 4 and move[1] == "x"):
            output=pieceTakes(output, move, color)
        else:
            if(len(move) == 4):
                if move[2] == '=':
                    # e.g a8=Q
                    output = pawnPromote(board, move, color)
                else:
                    # e.g Nbd3
                    output = moveByLocationHint(output, board, move, color)

            elif(len(move)==3):
                # a piece move to a empty cell, e.g Rb1, Bd7
                output = normalPieceMove(output, move)
            else:
                # TODO
                print("????!!!??")
                print('MOVE: ', move)
                print("!!!!!????!!!")
                try:
                    output['piece']=move[0]
                except:
                    output['piece']="exception piece"
                output['previousCell']="saved location of row or col:"+move[1]
                output['nextCell']=move[3:]
                output['takes']=True

    return output

# get output of normal piece move like Nb3
def normalPieceMove(output, move):
    output['piece']=move[0]
    output['previousCell']="previousCell"
    output['nextCell']=move[1:]

    return output

# get output of move by location hint like Nbd3
def moveByLocationHint(output, board, move, color):
    output['piece'] = move[0]
    locationHint = move[1]
    if locationHint.isnumeric():
        # find the piece in row of locationHint
        output['previousCell'] = findCellByRowLocation(board, color+output['piece'], locationHint)
    else:
        # find the piece in col of locationHint
        output['previousCell'] = findCellByColLocation(board, color+output['piece'], locationHint)
    output['nextCell']=move[2:]

    return output

# get output of pawn promotion move, a1=Q
def pawnPromote(board, move, color):
    promoteTo = move[3]
    move = move[:2]
    output = makeMove(board, move, color=color)
    output['promotion'] = promoteTo

    return output

# get outputs of short castling, O-O
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

# get outputs of long castling, O-O-O
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

# get output of forward pawn move like e4
def pawnForward(output, move, color):
    output['nextCell']=move
    output['piece']='p'
    print('move:', move)
    print('color:', color)
    if (move[1] == "4" and color == 'W'):
        output['previousCell']=[move[0]+"3", move [0]+"2"]
    elif (move[1] == "5" and color == 'B'):
        output['previousCell']=[move[0]+"6", move [0]+"7"]
    elif (color == 'W'):
        output['previousCell']=move[0]+str((int(move[1])-1))
    else:
        # black
        print('i am here')
        output['previousCell']=move[0]+str((int(move[1])+1))

    return output

# get output of piece takes move like Bxe3
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