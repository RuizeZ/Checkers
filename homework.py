import math
import copy
class Boardinfo:
    def __init__(self, gameBoard):
        self.whitePiece = 9
        self.blackPiece = 4
        self.whiteKingPiece = 0
        self.blackKingPiece = 0
        self.gameBoard = gameBoard
    
    def score(self):
        return self.whitePiece - self.blackPiece + (self.whiteKingPiece * 0.5 - self.blackKingPiece * 0.5)
    
    def allPieces(self, color):
        pieces = []
        for i in range(0,8):
            for j in range(0, 8):
                if self.gameBoard[i][j].lower() == color:
                    pieces.append([i, j])
        return pieces

    def move_piece(self, piece, oldrow, oldcol, newrow, newcol):
        self.gameBoard[oldrow][oldcol], self.gameBoard[newrow][newcol] =  self.gameBoard[newrow][newcol], self.gameBoard[oldrow][oldcol]
        if newrow == 0 or newrow == 7:
            if piece == "b":
                self.gameBoard[newrow][newcol] = "B"
                self.blackKingPiece += 1
            elif piece == "w":
                self.gameBoard[newrow][newcol] = "W"
                self.whiteKingPiece += 1
        
    def getValidMoves(self, color, isKing, oldrow, oldcol):
        leftDiagonal = oldcol - 1
        rightDiagonal = oldcol + 1
        validMoves = []
        if color == "b" or isKing:
            validMoves += (self.leftSide(oldrow + 1, min(oldrow + 3, 8), 1, color, leftDiagonal))
            validMoves += (self.rightSide(oldrow + 1, min(oldrow + 3, 8), 1, color, rightDiagonal))
            # print("valid moves")
            # print(validMoves)
        if color == "w" or isKing:
            validMoves += (self.leftSide(oldrow - 1, max(oldrow - 3, -1), -1, color, leftDiagonal))
            validMoves += (self.rightSide(oldrow - 1, max(oldrow - 3, -1), -1, color, rightDiagonal))
            # print("valid moves")
            # print(validMoves)
        return validMoves

    def leftSide(self, startrow, endrow, direction, color, left, jumpNode=[]):
        # print("in rightSide")
        # print("left jumpNode: ", jumpNode)
        validMoves = []
        previous = []
        
        if startrow > 7  or startrow < 0:
            return validMoves
        for i in range(startrow, endrow, direction):
            # print("prev", previous)
            if left < 0:
                break
            # print("[i][left]: ", i, left)
            if self.gameBoard[i][left].lower() == color:
                # print("same color")
                break
            
            #current is a empty square
            elif self.gameBoard[i][left] == '.': 
                #after one jumpNode, left is . 
                if jumpNode and not previous:
                    break
                #after one jumpNode, left is another color
                elif jumpNode:
                    pass
                    # validMoves[(i, left)] = previous + jumpNode
                #didnot jumpNode at all
                elif not previous and not jumpNode:
                    finalPosition = [i, left]
                    finalPosition.append(jumpNode)
                    validMoves.append(finalPosition)
                #it is possible to jumpNode
                if previous:
                    jumpNode.append(previous)
                    validMovesLength = len(validMoves)
                    if direction == -1:
                        next_endrow = max(i - 3, -1)
                    else:
                        next_endrow = min(i + 3, 8)
                    validMoves += (self.leftSide(i + direction, next_endrow, direction, color, left - 1, jumpNode))
                    # print("validMoves: ", validMoves)
                    # print("jumpNode: ", jumpNode)
                    validMoves += (self.rightSide(i + direction, next_endrow, direction, color, left + 1, jumpNode))
                    # print("validMoves: ", validMoves)
                    # print("jumpNode: ", jumpNode)
                    if len(validMoves) == validMovesLength:
                        finalPosition = [i, left]
                        new_jumpNode = jumpNode.copy()
                        finalPosition.append(new_jumpNode)
                        validMoves.append(finalPosition)
                        # print("validMoves.append(finalPosition): ",validMoves)
                    jumpNode.pop(-1)
                break
            #it is another color, and it is possible to jumpNode
            else:
                previous = [i, left]
            left -= 1
        return validMoves

    def rightSide(self, startrow, endrow, direction, color, right, jumpNode=[]):
        # print("in rightSide")
        # print("right jumpNode: ", jumpNode)
        validMoves = []
        previous = []
        
        if startrow > 7  or startrow < 0:
            return validMoves
        for i in range(startrow, endrow, direction):
            # print("prev", previous)
            if right > 7:
                break
            # print("[i][right]: ", i, right)
            if self.gameBoard[i][right].lower() == color:
                # print("same color")
                break
            
            #current is a empty square
            elif self.gameBoard[i][right] == '.': 
                #after one jumpNode, right is . 
                if jumpNode and not previous:
                    break
                #after one jumpNode, right is another color
                elif jumpNode:
                    # validMoves[(i, right)] = previous + jumpNode
                    pass
                elif not previous and not jumpNode:
                    finalPosition = [i, right]
                    finalPosition.append(jumpNode)
                    validMoves.append(finalPosition)
                # print("in right validMoves: ", validMoves)
                #it is possible to jumpNode
                if previous:
                    jumpNode.append(previous)
                    validMovesLength = len(validMoves)
                    if direction == -1:
                        next_endrow = max(i - 3, -1)
                    else:
                        next_endrow = min(i + 3, 8)
                    validMoves += (self.rightSide(i + direction, next_endrow, direction, color, right + 1, jumpNode))
                    validMoves += (self.leftSide(i + direction, next_endrow, direction, color, right - 1, jumpNode))
                    if len(validMoves) == validMovesLength:
                        finalPosition = [i, right]
                        new_jumpNode = jumpNode.copy()
                        finalPosition.append(new_jumpNode)
                        validMoves.append(finalPosition)
                        # print("validMoves.append(finalPosition): ",validMoves)
                    jumpNode.pop(-1)
                break
            #it is another color, and it is possible to jumpNode
            else:
                previous = [i, right]
            right += 1
        return validMoves
    
    def remove(self, removePieces):
        newlist = removePieces[2:][0]

        # print(newlist)
        for piece in newlist:
            # print(piece)
            if self.gameBoard[piece[0]][piece[1]] == 'W':
                self.whiteKingPiece -= 1
                self.whitePiece -= 1
            elif self.gameBoard[piece[0]][piece[1]] == 'w':
                self.whitePiece -= 1
            elif self.gameBoard[piece[0]][piece[1]] == 'B':
                self.blackKingPiece -= 1
                self.blackPiece -= 1
            elif self.gameBoard[piece[0]][piece[1]] == 'b':
                self.blackPiece -= 1
            self.gameBoard[piece[0]][piece[1]] = '.'

    def win(self):
        if self.blackPiece <= 0:
            return 'w'
        elif self.whitePiece <= 0:
            return 'b'
        else:
            return False

class during_game:
    def __init__(self, gameBoard, color):
        self.board = Boardinfo(gameBoard)
        self.turn = "b"
        self.validMoves = []
        self.selected = None
        self.color = color
        self.isKing = False
    
    def selectedPiece(self):
        oldrow, oldcol = input("which piece do you try to move?").split()
        oldrow = int(oldrow)
        oldcol = int(oldcol)
        piece = self.board.gameBoard[oldrow][oldcol]
        if piece.lower() == self.color:
            if piece.isupper():
                self.isKing = True
            else:
                self.isKing = False
            self.selected = piece
        else:
            print("not your color")
            self.selectedPiece()
            return 1

        if self.selected:
            self.validMoves = self.board.getValidMoves(self.color, self.isKing, oldrow, oldcol)
            # print("self.validMoves")
            # print(self.validMoves)
            newrow, newcol = input("where do you want the piece move to?").split()
            newrow, newcol = int(newrow), int(newcol)
            result = self.move(oldrow, oldcol, newrow, newcol)
            if not result:
                print("Faile to move")
                self.selected = None
                self.selectedPiece()

    def move(self, oldrow, oldcol, newrow, newcol):
        canbemoved = False
        for i in self.validMoves:
            if i[0] == newrow and i[1] == newcol:
                removepieces = i
                # print("i: ",i)
                canbemoved = True
                break
        if self.board.gameBoard[newrow][newcol] == '.' and canbemoved:
            self.board.move_piece(self.selected, oldrow, oldcol, newrow, newcol)
            jump = removepieces
            if jump:
                self.board.remove(jump)
            output(self.board.gameBoard)
        else:
            return False
        return True

    def getCurrentBoard(self):
        return self.board

    def afterAIMove(self, gameBoard):
        self.board = gameBoard
        output(self.board.gameBoard)

def allMoves(curBoard, color, game):
    moves = []
    for piece in curBoard.allPieces(color):
        if curBoard.gameBoard[piece[0]][piece[1]].isupper():
            isKing = True
        else:
            isKing = False
        validMoves = curBoard.getValidMoves(color, isKing, piece[0], piece[1])
        for validMove in validMoves:
            destination = validMove[:2]
            tempBoard = copy.deepcopy(curBoard)
            newBoard = afterTempMove(color, piece, destination,tempBoard, game, validMove)
            moves.append(newBoard)
    # print("moves")
    # print(moves)
    return moves

def afterTempMove(color, piece, destination, tempBoard, game, jump):
    tempBoard.move_piece(color, piece[0], piece[1], destination[0], destination[1])
    if jump:
        tempBoard.remove(jump)
    return tempBoard


def maxvalue(curBoard, curDepth, game, myColor, oppositColor):
    
    if curDepth == 0 or curBoard.win() != False:
        return curBoard.score(), curBoard
    nextMove = None
    maxScore = -100000
    for move in allMoves(curBoard, myColor, game):
        score = minvalue(move, curDepth - 1, game, myColor, oppositColor)[0]
        maxScore = max(maxScore, score)
        if maxScore == score:
            nextMove = move
    return maxScore, nextMove

def minvalue(curBoard, curDepth, game, myColor, oppositColor):
    if curDepth == 0 or curBoard.win() != False:
        return curBoard.score(), curBoard
    nextMove = None
    minScore = 100000
    for move in allMoves(curBoard, oppositColor, game):
        score = maxvalue(move, curDepth - 1, game, myColor, oppositColor)[0]
        minScore = min(minScore, score)
        if minScore == score:
            nextMove = move
    return minScore, nextMove

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
if myColor == 'b':
    maxScore, nextMove = maxvalue(game.getCurrentBoard(), 3, game, 'b', 'w')
    game.afterAIMove(nextMove)
else:
    maxScore, nextMove = maxvalue(game.getCurrentBoard(), 3, game, 'w', 'b')
    game.afterAIMove(nextMove)