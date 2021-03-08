import math 
class Boardinfo:
    def __init__(self, gameBoard):
        self.whitePiece = 12
        self.blackPiece = 12
        self.whiteKingPiece = 0
        self.blackKingPiece = 0
        self.gameBoard = gameBoard

    def move_piece(self, piece, oldrow, oldcol, newrow, newcol, gameBoard):
        gameBoard[oldrow][oldcol], gameBoard[newrow][newcol] =  gameBoard[newrow][newcol], gameBoard[oldrow][oldcol]
        if newrow == 0 or newrow == 7:
            if piece == "b":
                gameBoard[newrow][newcol] = "B"
                self.blackKingPiece += 1
            else:
                gameBoard[newrow][newcol] = "W"
                self.whiteKingPiece += 1
        output(gameBoard)

class during_game:
    def __init__(self, gameBoard, color):
        self.board = Boardinfo(gameBoard)
        self.turn = "b"
        self.validMoves = []
        self.selected = None
        self.color = color
    
    def selectedPiece(self):
        oldrow, oldcol = input("which piece do you try to move?").split()
        oldrow = int(oldrow)
        oldcol = int(oldcol)
        piece = self.board.gameBoard[oldrow][oldcol]
        if piece.lower() == self.color:
            if piece.isupper():
                isKing = True
            else:
                isKing = False
            self.selected = piece
        else:
            self.selectedPiece()

        if self.selected:
            newrow, newcol = input("where do want the piece move to?").split()
            newrow, newcol = int(newrow), int(newcol)
            self.validMoves.append([newrow, newcol])
            result = self.move(oldrow, oldcol, newrow, newcol)
            if not result:
                self.selected = None
                self.selectedPiece()
        # else:
        #     piece = self.board.gameBoard[row][col]
        #     self.selected = piece
        #     self.validMoves = self.board.getValidMoves(row, col)


    def move(self, oldrow, oldcol, newrow, newcol):
        if self.board.gameBoard[newrow][newcol] == '.' and [newrow, newcol] in self.validMoves:
            self.board.move_piece(self.selected, oldrow, oldcol, newrow, newcol, gameBoard)
        else:
            return False
        return True



class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.isking = False

    def become_king(self):
        self.isking = True
    
    def after_move(self, row, col):
        self.row = row
        self.col = col
    


  
def maxvalue(curDepth, nodeIndex, scores, targetDepth):
    if (curDepth == targetDepth):  
        return scores[nodeIndex]
    v = -100000
    curDepth += 1
    for i in range(nodeIndex * 2, nodeIndex * 2 + 2):
        v = max(v, minvalue(curDepth, i, scores, targetDepth))
    return v

def minvalue(curDepth, nodeIndex, scores, targetDepth):
    if (curDepth == targetDepth):  
        return scores[nodeIndex]
    v = 100000
    curDepth += 1
    for i in range(nodeIndex * 2, nodeIndex * 2 + 2):
        v = min(v, maxvalue(curDepth, i, scores, targetDepth))
    return v

def output(gameBoard):
    line = 0
    outputStr = ""
    f = open("output.txt", "a")
    for position in gameBoard:
        line += 1
        if line == 8:
            outputStr += ''.join(position)
        else:
            outputStr += ''.join(position) + "\n"
    f.write(outputStr)
    f.close()

#read input file
lineNum = 0
currentrow = 0
gameBoard = []
inputFile = open("input.txt", "r")
outputFile = open("output.txt", "w")
for line in inputFile:
    lineNum += 1 
    if lineNum == 1:
        mode = line.strip("\n")
    elif lineNum == 2:
        myColor = line.strip("\n")
    elif lineNum == 3:
        timeRemain = float(line)
    else:
        gameBoard.append(list(line.strip("\n")))
print("mode is", mode)
print("myColor is", myColor)
print("timeRemain is", timeRemain)
print("gameBoard is:")
print(gameBoard)
if myColor == "BLACK":
    myColor = 'b'
else:
    myColor = 'w'
game = during_game(gameBoard, myColor)
# board.move_piece(piece, 0, 1, 7, 0, gameBoard)
game.selectedPiece()