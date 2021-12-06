class Line():
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.passedX = [x for x in range(min(self.x1, self.x2), max(self.x1, self.x2) + 1)]
        self.passedY = [x for x in range(min(self.y1, self.y2), max(self.y1, self.y2) + 1)]
        
        #Reverse list if line goes up or from right to left
        if self.x1 > self.x2:
            self.passedX.reverse()
        if self.y1 > self.y2:
            self.passedY.reverse()

        if not (self.isVertical() or self.isHorizontal()):
            self.passedPoints = list(zip(self.passedX, self.passedY))
        elif self.isHorizontal():
            self.passedPoints = list((x, self.y1) for x in self.passedX)
        elif self.isVertical():
            self.passedPoints = list((self.x1, y) for y in self.passedY)


    def __repr__(self):
        return f"{self.x1}.{self.y1} -> {self.x2}.{self.y2}"

    def isHorizontal(self):
        return self.y1 == self.y2

    def isVertical(self):
        return self.x1 == self.x2

    def checkIntersect(self, other):
        return set(self.passedPoints) & set(other.passedPoints)



INPUTFILE = "input.txt"

def readInput():
    Lines = []
    with open(INPUTFILE, "r") as f:
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            l = line.split(" -> ")
            z = [[int(a) for a in x.split(",")] for x in l]
            Lines.append(Line(z[0][0], z[0][1], z[1][0], z[1][1]))
    return Lines


def solution1():
    LinesAll = readInput()
    LinesH = [l for l in LinesAll if l.isHorizontal()]
    LinesV = [l for l in LinesAll if l.isVertical()]
    LinesHV = LinesH + LinesV
    crossPoints = []
    for L in LinesHV:
        for L2 in LinesHV:
            if L != L2:
                intersect = L.checkIntersect(L2)
                if len(intersect) > 0:
                    crossPoints.extend(list(intersect))
    return len(list(set(crossPoints)))


def solution2():
    LinesAll = readInput()
    crossPoints = []
    for L in LinesAll:
        for L2 in LinesAll:
            if L != L2:
                intersect = L.checkIntersect(L2)
                if len(intersect) > 0:
                    crossPoints.extend(list(intersect))
    return len(list(set(crossPoints)))

print(solution1())
print(solution2())
