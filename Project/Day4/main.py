
class Number():
    def __init__(self, value):
        self.value = value
        self.passed = False
        return None
    def passed(self):
        self.passed = True
        return None
    def __repr__(self):
        return str(self.value) + " " + str(self.passed)

class Board():
    def __init__(self, board): #expect board as list of lists eg. [[1,2,3],[3,1,2]] is 1,2,3
                               #                                                       3,1,2
        self.board = []
        for row in board:
            row.strip("\n")
            row = row.split(" ")
            x = [y for y in row if len(y) > 0]
            x = [Number(int(y)) for y in x]
            self.board.append(x)
        return None

    def __repr__(self):
        r = ""
        for x in self.board:
            x = [str(y) for y in x]
            x = " ".join(x)
            r += x + "\n"
        return r

    def checkValue(self, value):
        for row in self.board:
            for number in row:
                if number.value == value:
                    number.passed = True
        return None

    def checkWin(self):
        for row in self.board:
            rowPassed = sum([int(x.passed) for x in row]) #count all passed in 1 row
            if rowPassed == len(row):
                return True
        for i in range(0,len(self.board[0])):
            columnPassed = sum(list(map(lambda x: int(x[i].passed), self.board))) # count all passed in 1 columns. Map functions takes every i'th element from row
            if columnPassed == len(self.board):
                return True
        return False

    def getAllNonCalledValues(self):
        x = []
        for row in self.board:
            for i in row:
                if not i.passed:
                    x.append(i.value)
        return x

    def reset(self):
        for row in self.board:
            for i in row:
                i.passed = False
        return None



def readInput():
    with open(INPUTFILE, "r") as f:
        bingoNumber = [int(x) for x in f.readline().split(",")]
        boards = []
        Y = True
        while Y:
            _ = f.readline()
            x = []
            for i in range(0,5):
               z = f.readline().strip()
               if len(z) == 0:
                   Y = False
                   break
               x.append(z)
            if len(x) != 0:
                boards.append(Board(x))
        return bingoNumber, boards

def runGame1(bingoNumber, boards, debug=False):
    for bingo in bingoNumber:
        for i in boards:
            i.checkValue(bingo)
            if i.checkWin():
                return i, bingo
            if debug:
                print(bingo, i, sep="\n")
                input("")

def runGame2(bingoNumber, boards):
    for bingo in bingoNumber:
        for i in boards:
            i.checkValue(bingo)
            if i.checkWin():
                boards = [x for x in boards if x != i]
                if len(boards) == 1:
                    return boards


INPUTFILE = "input.txt"

def solution1():
    bingoNumber, boards = readInput()
    winningBoard, winningBingo = runGame1(bingoNumber, boards)
    nonCalledSum = sum(winningBoard.getAllNonCalledValues())
    print(nonCalledSum * winningBingo)

def solution2():
    bingoNumber, boards = readInput()
    lastWinning = runGame2(bingoNumber, boards) # get list with only the last winning board
    lastWinning[0].reset()
    lastWinning, lastBingo = runGame1(bingoNumber, lastWinning, debug=False) #replay game with only that board to get answers
    nonCalledSum = sum(lastWinning.getAllNonCalledValues())
    print(nonCalledSum, lastBingo)
    print(nonCalledSum * lastBingo)


solution1()
solution2()
