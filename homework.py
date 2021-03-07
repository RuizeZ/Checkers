# A simple Python3 program to find 
# maximum score that 
# maximizing player can get 
import math 
  
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
#def minimax (curDepth, nodeIndex, maxTurn, scores, targetDepth):

  
#     # base case : targetDepth reached 
#     if (curDepth == targetDepth):  
#         return scores[nodeIndex] 
      
#     if (maxTurn): 
#         return max(minimax(curDepth + 1, nodeIndex * 2,  
#                     False, scores, targetDepth),  
#                    minimax(curDepth + 1, nodeIndex * 2 + 1,  
#                     False, scores, targetDepth)) 
      
#     else: 
#         return min(minimax(curDepth + 1, nodeIndex * 2,  
#                      True, scores, targetDepth),  
#                    minimax(curDepth + 1, nodeIndex * 2 + 1,  
#                      True, scores, targetDepth)) 
      
# Driver code 
scores = [3, 5, 2, 9, 12, 5, 23, 23] 
  
treeDepth = math.log(len(scores), 2) 
  
print("The optimal value is : ", end = "") 
print(maxvalue(0, 0, scores, treeDepth))
  
# This code is contributed 
# by rootshadow 



#read input file
# lineNum = 0
# currentrow = 0
# gameBoard = []
# inputFile = open("input.txt", "r")
# outputFile = open("output.txt", "w")
# for line in inputFile:
#     lineNum += 1 
#     if lineNum == 1:
#         mode = line.strip("\n")
#     elif lineNum == 2:
#         myColor = line.strip("\n")
#     elif lineNum == 3:
#         timeRemain = float(line)
#     else:
#         gameBoard.append(list(line.split()))
# print("mode is", mode)
# print("myColor is", myColor)
# print("timeRemain is", timeRemain)
# print("gameBoard is:")
# print(gameBoard)