from timer import time

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
        l = [int(x) for x in f.readline().strip().split(",")]
    return l

def runSim(days, fish):
    for i in range(0,days):
        reproducing = fish.pop()
        fish.list[6] += reproducing # reset timer to 6
        fish.list[8] += reproducing # add fish with timer 8
    print(f"# Solution after {days}: {sum(fish.list)}")

def runSimV2(days, inputFile):
    l = [0]*9
    a = readInput(inputFile)
    for i in set(a): l[i] += a.count(i)
    for i in range(0,days):
        reproducing = l.pop(0)
        l[6] += reproducing # reset timer to 6
        l.append(reproducing) # add fish with timer 8
    print(f"# Solution after {days}: {sum(l)}")

@time
def solution1():
    l = readInput("input.txt")
    fish = FishList(l)
    runSim(80, fish)

@time
def solution2():
    l = readInput("input.txt")
    fish = FishList(l)
    runSim(256, fish)

@time
def solution1v2():
    runSimV2(80, "input.txt")

@time
def solution2v2():
    runSimV2(256, "input.txt")

solution1()
solution2()
solution1v2()
solution2v2()
# Solution after 80: 373378
# Function solution1(): time elapsed: 0.375 [ms]
# Solution after 256: 1682576647495
# Function solution2(): time elapsed: 0.203 [ms]
# Solution after 80: 373378
# Function solution1v2(): time elapsed: 0.108 [ms]
# Solution after 256: 1682576647495
# Function solution2v2(): time elapsed: 0.134 [ms]
