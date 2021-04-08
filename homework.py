import math
import copy
import time
class Boardinfo:
    def __init__(self, gameBoard, blackPiece, whitePiece, blackKingPiece, whiteKingPiece):
        self.whitePiece = whitePiece
        self.blackPiece = blackPiece
        self.whiteKingPiece = whiteKingPiece
        self.blackKingPiece = blackKingPiece
        self.gameBoard = gameBoard
    
    def score(self, color):
        blackKingscore = self.blackKingPiece * 80
        whiteKingscore = self.whiteKingPiece * 80
        nextblackKingscore = 0
        nextwhiteKingscore = 0
        blackPiesesScore = (self.blackPiece - self.blackKingPiece) * 30
        whitePiesesScore = (self.whitePiece - self.whiteKingPiece) * 30
        blackBackRow = 0
        whiteBackRow = 0
        blackInMiddle = 0
        whiteInMiddle = 0
        blackInDanger = 0
        whiteInDanger = 0
        blackProtected = 0
        whiteProtected = 0
        blackDoubleCorner = 0
        whiteDoubleCorner = 0
        blackAttackDoubleCorner = 0
        whiteAttackDoubleCorner = 0
        blackPieces = []
        whitePieces = []
        maxDistance = 0
        totalPieces = self.whitePiece + self.blackPiece
        for i in range(0,8):
            for j in range(0, 8):
                if self.gameBoard[i][j] == 'b' or self.gameBoard[i][j] == 'B':
                    blackPieces.append([i, j])
                    if self.gameBoard[i][j] == 'b':
                        blackPiesesScore += i
                        if i == 0:
                            if j == 0 or j == 7:
                                blackBackRow += 8
                            else:
                                blackBackRow += 10
                        if (i == 0 and j == 1) or (i == 1 and j == 0):
                            blackDoubleCorner += 4
                        if (i > 4) and (j > 4):
                            blackAttackDoubleCorner += 2
                        if i == 6 and j != 7:
                            if self.gameBoard[i + 1][j - 1] == '.' and self.gameBoard[i + 1][j + 1] == '.':
                                nextblackKingscore += 15
                        if i == 6 and j == 7:
                            if self.gameBoard[i + 1][j - 1] == '.':
                                nextblackKingscore += 15
                    if (i == 3 or i == 4):
                        if (j > 1 and j < 6 ):
                            blackInMiddle += 4
                        else:
                            blackInMiddle -= 2

                    if i != 0 and i != 7:
                        if (j != 0 and j != 7):
                            if ((self.gameBoard[i + 1][j - 1] == 'w' or self.gameBoard[i + 1][j - 1] == 'W') and self.gameBoard[i - 1][j + 1] == '.')  or ((self.gameBoard[i + 1][j + 1] == 'w' or self.gameBoard[i + 1][j + 1] == 'W') and self.gameBoard[i - 1][j - 1] == '.'):
                                blackInDanger -= 15
                            elif (self.gameBoard[i - 1][j - 1] == 'W' and self.gameBoard[i + 1][j + 1] == '.') or (self.gameBoard[i - 1][j + 1] == 'W' and self.gameBoard[i + 1][j - 1] == '.'):
                                blackInDanger -= 15

                        if (j == 0 or j == 7):
                            blackProtected += 15
                        elif (self.gameBoard[i - 1][j - 1] != '.' and (not self.gameBoard[i - 1][j - 1].isupper())) and (self.gameBoard[i - 1][j + 1] != '.' and (not self.gameBoard[i - 1][j + 1].isupper())):
                            blackProtected += 15
                    

                elif self.gameBoard[i][j] == 'w'or self.gameBoard[i][j] == 'W':
                    whitePieces.append([i, j])
                    if self.gameBoard[i][j] == 'w':
                        whitePiesesScore += 7-i
                        if i == 7:
                            if j == 0 or j == 6:
                                whiteBackRow += 8
                            else:
                                whiteBackRow += 10
                        if (i == 7 and j == 6) or (i == 6 and j == 7):
                            whiteDoubleCorner += 4
                        if (i < 3) and (j < 3):
                            whiteAttackDoubleCorner += 2
                        if i == 1 and j != 0:
                            if self.gameBoard[i - 1][j - 1] == '.' and self.gameBoard[i - 1][j + 1] == '.':
                                nextwhiteKingscore += 15
                        elif i == 1 and j == 0:
                            if self.gameBoard[i - 1][j + 1] == '.':
                                nextwhiteKingscore += 15
                    if (i == 3 or i == 4):
                        if (j > 1 and j < 6 ):
                            whiteInMiddle += 4
                        else:
                            whiteInMiddle -= 2

                    if i != 0 and i != 7:
                        if (j != 0 and j != 7):
                            if ((self.gameBoard[i - 1][j - 1] == 'b' or self.gameBoard[i - 1][j - 1] == 'B') and self.gameBoard[i + 1][j + 1] == '.') or ((self.gameBoard[i - 1][j + 1] == 'b' or self.gameBoard[i - 1][j + 1] == 'B') and self.gameBoard[i + 1][j - 1] == '.'):
                                whiteInDanger -= 15
                            elif (self.gameBoard[i + 1][j - 1] == 'B' and self.gameBoard[i - 1][j + 1] == '.') or (self.gameBoard[i + 1][j + 1] == 'B' and self.gameBoard[i - 1][j - 1] == '.'):
                                whiteInDanger -= 15

                        if (j == 0 or j == 7):
                            whiteProtected += 15
                        elif (self.gameBoard[i + 1][j - 1] != '.' and (not self.gameBoard[i + 1][j - 1].isupper())) and (self.gameBoard[i + 1][j + 1] != '.' and (not self.gameBoard[i + 1][j + 1].isupper())):
                                whiteProtected += 15
                    

        blackTotalScore = blackPiesesScore + blackKingscore + blackBackRow + blackInMiddle + blackInDanger + blackProtected + nextblackKingscore + blackDoubleCorner + blackAttackDoubleCorner
        whiteTotalScore = whitePiesesScore + whiteKingscore + whiteBackRow + whiteInMiddle + whiteInDanger + whiteProtected + nextwhiteKingscore + whiteDoubleCorner + whiteAttackDoubleCorner

        if color == 'b':
            if totalPieces < 9:
                for i in blackPieces:
                    row = i[0]
                    column = i[1]
                    if self.gameBoard[row][column].isupper():
                        for j in whitePieces:
                            distance = math.hypot(j[0] - row, j[1] - column)
                            maxDistance = max(maxDistance, distance)
            
            score = (blackTotalScore - whiteTotalScore - (maxDistance * 5)) / totalPieces
        if color == 'w':
            if totalPieces < 9:
                for i in whitePieces:
                    row = i[0]
                    column = i[1]
                    if self.gameBoard[row][column].isupper():
                        for j in blackPieces:
                            distance = math.hypot(j[0] - row, j[1] - column)
                            maxDistance = max(maxDistance, distance)
            score = (whiteTotalScore - blackTotalScore - (maxDistance * 5)) / totalPieces
        return score
    
    def allPieces(self, color):
        pieces = []
        for i in range(0,8):
            for j in range(0, 8):
                if self.gameBoard[i][j].lower() == color:
                    pieces.append([i, j])
        if color == 'w':
            pieces.reverse()
        # print("pieces: ",pieces)
        return pieces

    def move_piece(self, piece, oldrow, oldcol, newrow, newcol):
        self.gameBoard[oldrow][oldcol], self.gameBoard[newrow][newcol] =  self.gameBoard[newrow][newcol], self.gameBoard[oldrow][oldcol]
        if piece == "b" and newrow == 7 and self.gameBoard[newrow][newcol] != "B":
            self.gameBoard[newrow][newcol] = "B"
            self.blackKingPiece += 1
        elif piece == "w" and newrow == 0 and self.gameBoard[newrow][newcol] != "W":
            self.gameBoard[newrow][newcol] = "W"
            self.whiteKingPiece += 1
        # print(self.gameBoard)
        
    def getValidMoves(self, color, isKing, oldrow, oldcol):
        leftDiagonal = oldcol - 1
        rightDiagonal = oldcol + 1
        validJumpMoves = []
        TempvalidMoves = []
        validMoves = []
        
        if color == "b" or isKing:
            TempvalidMoves += (self.leftSide(oldrow, oldcol, oldrow + 1, min(oldrow + 3, 8), 1, color, leftDiagonal, isKing))
            TempvalidMoves += (self.rightSide(oldrow, oldcol, oldrow + 1, min(oldrow + 3, 8), 1, color, rightDiagonal, isKing))

        if color == "w" or isKing:
            TempvalidMoves += (self.leftSide(oldrow, oldcol, oldrow - 1, max(oldrow - 3, -1), -1, color, leftDiagonal, isKing))
            TempvalidMoves += (self.rightSide(oldrow, oldcol, oldrow - 1, max(oldrow - 3, -1), -1, color, rightDiagonal, isKing))
        for i in TempvalidMoves:
            i.insert(0, [oldrow, oldcol])
            if len(i) > 3:
                validJumpMoves.append(i)
            else:
                validMoves.append(i)
        # print(validJumpMoves)
        return validMoves, validJumpMoves
        

    def leftSide(self, oldrow, oldcol, startrow, endrow, direction, color, left, isKing, jumpNode=[], nextPositionList=[]):
        validMoves = []
        previous = []
        backToOriginal = False
        if startrow > 7  or startrow < 0:
            return validMoves
        for i in range(startrow, endrow, direction):
            if left < 0:
                break
            if self.gameBoard[i][left].lower() == color:
                if i == oldrow and left == oldcol:
                    backToOriginal = True
                else:
                    backToOriginal = False
            if self.gameBoard[i][left].lower() == color and not backToOriginal:
                    break
            elif [i, left] in jumpNode:
                return validMoves
            #current is a empty square
            elif self.gameBoard[i][left] == '.' or backToOriginal: 
                #after one jumpNode, left is . 
                if jumpNode and not previous:
                    break
                #after one jumpNode, left is another color
                elif jumpNode:
                    pass
                #didnot jumpNode at all
                elif not previous and not jumpNode:
                    finalPosition = []
                    finalPosition.append([i, left])
                    finalPosition.append(jumpNode)
                    validMoves.append(finalPosition)

                #it is possible to jumpNode
                if previous:
                    nextPosition = []
                    nextPosition.append(previous[0] + direction)
                    nextPosition.append(previous[1] - 1)
                    nextPositionList.append(nextPosition)
                    jumpNode.append(previous)
                    validMovesLength = len(validMoves)
                    if direction == -1:
                        next_endrow = max(i - 3, -1)
                    else:
                        next_endrow = min(i + 3, 8)
                    validMoves += (self.leftSide(oldrow, oldcol, i + direction, next_endrow, direction, color, left - 1, isKing, jumpNode, nextPositionList))
                    validMoves += (self.rightSide(oldrow, oldcol, i + direction, next_endrow, direction, color, left + 1, isKing, jumpNode, nextPositionList))
                    if isKing:
                        if direction == -1:
                            next_endrow = min(i + 3, 8)
                        else:
                            next_endrow = max(i - 3, -1)
                        validMoves += (self.leftSide(oldrow, oldcol, i + (-direction), next_endrow, -direction, color, left - 1, isKing, jumpNode, nextPositionList))

                    if len(validMoves) == validMovesLength:
                        finalPosition = []
                        finalPosition.append([i, left])
                        new_jumpNode = jumpNode.copy()
                        new_nextPositionList = nextPositionList.copy()
                        finalPosition.append(new_jumpNode)
                        finalPosition.append(new_nextPositionList)
                        validMoves.append(finalPosition)

                    jumpNode.pop(-1)
                    nextPositionList.pop(-1)
                break
            #it is another color, and it is possible to jumpNode
            else:
                previous = [i, left]
            left -= 1
        return validMoves

    def rightSide(self, oldrow, oldcol, startrow, endrow, direction, color, right, isKing, jumpNode=[], nextPositionList=[]):
        backToOriginal = False
        validMoves = []
        previous = []
        if startrow > 7  or startrow < 0:
            return validMoves
        for i in range(startrow, endrow, direction):
            if right > 7:
                break
            if self.gameBoard[i][right].lower() == color:
                if i == oldrow and right == oldcol:
                    backToOriginal = True
                else:
                    backToOriginal = False
            if self.gameBoard[i][right].lower() == color and not backToOriginal:
                break
            elif [i, right] in jumpNode:
                return validMoves
            #current is a empty square
            elif self.gameBoard[i][right] == '.' or backToOriginal: 
                #after one jumpNode, right is . 
                if jumpNode and not previous:
                    break
                #after one jumpNode, right is another color
                elif jumpNode:
                    pass
                elif not previous and not jumpNode:
                    finalPosition = []
                    finalPosition.append([i, right])
                    finalPosition.append(jumpNode)
                    validMoves.append(finalPosition)
                #it is possible to jumpNode
                if previous:
                    nextPosition = []
                    nextPosition.append(previous[0] + direction)
                    nextPosition.append(previous[1] + 1)
                    nextPositionList.append(nextPosition)
                    jumpNode.append(previous)
                    validMovesLength = len(validMoves)
                    if direction == -1:
                        next_endrow = max(i - 3, -1)
                    else:
                        next_endrow = min(i + 3, 8)
                    
                    validMoves += (self.rightSide(oldrow, oldcol, i + direction, next_endrow, direction, color, right + 1, isKing, jumpNode, nextPositionList))
                    validMoves += (self.leftSide(oldrow, oldcol, i + direction, next_endrow, direction, color, right - 1, isKing, jumpNode, nextPositionList))
                    if isKing:
                        if direction == -1:
                            next_endrow = min(i + 3, 8)
                        else:
                            next_endrow = max(i - 3, -1)
                        validMoves += (self.rightSide(oldrow, oldcol, i + (-direction), next_endrow, -direction, color, right + 1, isKing, jumpNode, nextPositionList))
                        
                    if len(validMoves) == validMovesLength:
                        finalPosition = []
                        finalPosition.append([i, right])
                        new_jumpNode = jumpNode.copy()
                        new_nextPositionList = nextPositionList.copy()
                        finalPosition.append(new_jumpNode)
                        finalPosition.append(new_nextPositionList)
                        validMoves.append(finalPosition)
                    jumpNode.pop(-1)
                    nextPositionList.pop(-1)
                break
            #it is another color, and it is possible to jumpNode
            else:
                previous = [i, right]
            right += 1
        return validMoves
    
    def remove(self, removePieces):
        for piece in removePieces:
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

    def win(self, color):
        if color == 'b':
            if self.blackPiece <= 0:
                return -10000
            elif self.whitePiece <= 0:
                return 10000
        elif color == 'w':
            if self.blackPiece <= 0:
                return 10000
            elif self.whitePiece <= 0:
                return -10000     
        else:
            return False

class during_game:
    def __init__(self, gameBoard, color, blackPiece, whitePiece, blackKingPiece, whiteKingPiece):
        self.board = Boardinfo(gameBoard, blackPiece, whitePiece, blackKingPiece, whiteKingPiece)
        self.turn = "b"
        self.validMoves = []
        self.selected = None
        self.color = color
        self.isKing = False

    def getCurrentBoard(self):
        return self.board

    def afterAIMove(self, gameBoard):
        self.board = gameBoard[-1]
        # print("whitePiece: ", self.board.whitePiece)
        # print("blackPiece: ", self.board.blackPiece)
        # print("whiteKingPiece: ", self.board.whiteKingPiece)
        # print("blackKingPiece: ", self.board.blackKingPiece)
        # score = self.board.score(self.color)
        # print("score: ", score)
        output(self.board.gameBoard, gameBoard)

def allMoves(curBoard, color, game):
    moves = []
    validMoveperpiecelist = []
    validJumpMoveperpiecelist = []
    validMoves = []
    validJumpMoves = []
    
    for piece in curBoard.allPieces(color):
        validMoveperpiecelist.append(piece)
        validJumpMoveperpiecelist.append(piece)
        if curBoard.gameBoard[piece[0]][piece[1]].isupper():
            isKing = True
        else:
            isKing = False
        
        validMoveperpiece, validJumpMoveperpiece = curBoard.getValidMoves(color, isKing, piece[0], piece[1])

        if len(validMoveperpiece) != 0:
            validMoves += validMoveperpiece
        if len(validJumpMoveperpiece) != 0:
            validJumpMoves += validJumpMoveperpiece
    if validJumpMoves:
        validMoves = validJumpMoves
    # print("validMoves: ")
    # print(validMoves)
    for validMove in validMoves:
        # print("validMove: ")
        # print(validMove)
        newBoardPackage = []
        destination = validMove[1]
        tempBoard = copy.deepcopy(curBoard)
        newBoard = afterTempMove(color, validMove[0], destination,tempBoard, game, validMove[2])

        newBoardPackage = validMove.copy()
        newBoardPackage.append(newBoard)
        moves.append(newBoardPackage)
    
    return moves

def afterTempMove(color, piece, destination, tempBoard, game, jump):
    tempBoard.move_piece(color, piece[0], piece[1], destination[0], destination[1])
    if jump:
        tempBoard.remove(jump)
    return tempBoard


def maxvalue(curBoard, curDepth, game, myColor, oppositColor, alpha, beta):
    
    result = curBoard.win(myColor)
    if result != None:
        return result, curBoard
    elif curDepth == 0:
        # curBoard.win()
        return curBoard.score(myColor), curBoard
    nextMove = None
    maxScore = -100000
    scorelist = []
    for move in allMoves(curBoard, myColor, game):
        # print("in max")
        # print(move[-1].gameBoard)
        # print("")
        score = minvalue(move[-1], curDepth - 1, game, myColor, oppositColor, alpha, beta)[0]
        # print(" max curDepth: ", curDepth)
        # scorelist.append(score)
        maxScore = max(maxScore, score)
        # print("maxScore: ", maxScore)
        # print("maxScore: ", maxScore)
        if maxScore == score:
            nextMove = move
        if maxScore >= beta:
            # print("return max scorelist: ", scorelist)
            return maxScore, nextMove
        alpha = max(alpha, maxScore)
    # if curDepth == 10:
    #     print("max scorelist: ", scorelist)
    # output(nextMove[-1].gameBoard, 1)
    # print("nextMove[-1].score(myColor): ", nextMove[-1].score(myColor))
    return maxScore, nextMove

def minvalue(curBoard, curDepth, game, myColor, oppositColor, alpha, beta):
    
    result = curBoard.win(myColor)
    if result != None:
        return result, curBoard
    elif curDepth == 0:
        # curBoard.win()
        return curBoard.score(myColor), curBoard
    nextMove = None
    minScore = 100000
    scorelist = []
    
    for move in allMoves(curBoard, oppositColor, game):

        # print(move[-1].gameBoard)
        # print("")
        score = maxvalue(move[-1], curDepth - 1, game, myColor, oppositColor, alpha, beta)[0]
        scorelist.append(score)
        minScore = min(minScore, score)
        # print("minScore: ", minScore)
        if minScore == score:
            nextMove = move
        if minScore <= alpha:
            return minScore, nextMove
        beta = min(beta, minScore)
    # print("")

    #print("min scorelist: ", scorelist)    
    # output(nextMove[-1].gameBoard, 1)
    # print("nextMove: ", nextMove)
    # print("nextMove[-1].score(myColor): ", nextMove[-1].score(myColor))
    # if curDepth == 1:
    #     print("min scorelist: ", scorelist)
    return minScore, nextMove

def output(gameBoard, outputMoves):
    line = 0
    jumpTimes = -1
    outputStr = ""
    prev = ""
    f = open("output.txt", "a")
    start =  chr(97 + outputMoves[0][1]) + str(8 - outputMoves[0][0])
    end = chr(97 + outputMoves[1][1]) + str(8 - outputMoves[1][0])
    if len(outputMoves[2]) == 0:
        outputStr = "E " + start + " " + end
    else:
        # print(outputMoves[3])
        for i in outputMoves[3]:
            istr = chr(97 + i[1]) + str(8 - i[0])
            jumpTimes += 1
            if jumpTimes == 0:
                if len(outputMoves[3]) == 1:
                    outputStr = "J " + start + " " + istr
                else:
                    outputStr = "J " + start + " " + istr + "\n"
            else:
                if i == outputMoves[3][-1]:
                    outputStr += "J " + prev + " " + istr
                else:
                    outputStr += "J " + prev + " " + istr + "\n"
            prev = istr
    # outputStr += "\n"
    # for position in gameBoard:
    #     line += 1
    #     if line == 8:
    #         outputStr += ''.join(position)
    #     else:
    #         outputStr += ''.join(position) + "\n"
    f.write(outputStr)
    f.close()

#read input file
start_time = time.time()
lineNum = 0
currentrow = 0
blackKingPiece, whiteKingPiece, blackPiece, whitePiece = 0, 0, 0, 0
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
        for i in list(line.strip("\n")):
            if i == 'W':
                whiteKingPiece += 1
                whitePiece += 1
            elif i == 'w':
                whitePiece += 1
            elif i == 'B':
                blackKingPiece += 1
                blackPiece += 1
            elif i == 'b':
                blackPiece += 1
        gameBoard.append(list(line.strip("\n")))

if myColor == "BLACK":
    myColor = 'b'
else:
    myColor = 'w'

totalPieces = blackPiece + whitePiece
game = during_game(gameBoard, myColor, blackPiece, whitePiece, blackKingPiece, whiteKingPiece)
# print("totalPieces: ", totalPieces)
if mode == "SINGLE":
    deep = 1
else:
    if timeRemain < 5:
        deep = 6
    elif timeRemain <= 3:
        deep = 4
    elif totalPieces > 21:
        deep = 8
    elif totalPieces > 13:
        deep = 6
    elif totalPieces > 11:
        deep = 9
    elif totalPieces > 8:
        deep = 9
    elif totalPieces > 6:
        deep = 8
    elif totalPieces > 5:
        deep = 9
    else:
        deep = 9
# print("deep: ",deep)
if myColor == 'b':
    maxScore, nextMove = maxvalue(game.getCurrentBoard(), deep, game, 'b', 'w', -10000, 10000)
    # print("nextMove: ")
    # print(nextMove)
    # print("maxScore: ")
    # print(maxScore)
    if type(nextMove) is list:
        game.afterAIMove(nextMove)
else:
    maxScore, nextMove = maxvalue(game.getCurrentBoard(), deep, game, 'w', 'b', -10000, 10000)
    # print("nextMove: ")
    # print(nextMove)
    # print(nextMove[-1].score('w'))
    # print("maxScore: ") 
    # print(maxScore)
    
    if type(nextMove) is list:
        game.afterAIMove(nextMove)
# print("--- %s seconds ---" % (time.time() - start_time))