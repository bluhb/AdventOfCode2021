
class FishList():
    def __init__(self, initialState):
        self.list = [0 for _ in range(0,9)]
        for i in initialState:
            self.list[i] += 1
        return None

    def __repr__(self):
        return str([str(x+1) * self.list[x] for x in range(0,7)])

    def pop(self):
        r = self.list.pop(0)
        self.list.append(0)
        return r

def readInput(inputFile):
    with open(inputFile, "r") as f:
        l = f.readline().strip()
        l = [int(x) for x in l.split(",")]
    return l

def runSim(days, fish):
    for i in range(0,days):
        reproducing = fish.pop()
        fish.list[6] += reproducing # reset timer to 6
        fish.list[8] += reproducing # add fish with timer 8
    print(sum(fish.list))

def solution1():
    l = readInput("input.txt")
    fish = FishList(l)
    runSim(80, fish)

def solution2():
    l = readInput("input.txt")
    fish = FishList(l)
    runSim(256, fish)

solution1()
solution2()
