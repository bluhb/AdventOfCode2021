
def solution1():
    with open(INPUTFILE, "r") as f:
        lastNum = None
        increased = 0
        for line in f:
            line = int(line)
            if lastNum is not None:
                if line > lastNum:
                    increased += 1
            lastNum = line
        return(f"Increased: {increased}")

def solution2():
    def createWindow(start, length, data):
        z = sum(data[start:start+length])
        return z

    f = open(INPUTFILE, "r").readlines()
    f = [int(x) for x in f]
    increased = 0
    for i in range(0, len(f)-3):
        a = createWindow(i, 3, f)
        b = createWindow(i+1, 3, f)
        if b > a:
            increased += 1
    return(f"Increased: {increased}")


if __name__ == "__main__":
    INPUTFILE = "input.txt"
    print(solution1())
    print(solution2())
