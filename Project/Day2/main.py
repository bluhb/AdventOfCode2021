import re as r


INPUTFILE = "input.txt"

def solution1():
    with open(INPUTFILE, "r") as f:
        location = {"x":0, "y":0}
        for line in f:
            d = r.search("(\w*) *(\d*)", line)
            direction = lambda x : "x" if x == "forward" else "y"
            plus_min = lambda x,y : int(x) if y in ["down", "forward"] else int(x)*-1

            d = [direction(d.group(1)), plus_min(d.group(2), d.group(1))]
            location[d[0]] += d[1]
    return f"Solution1: {location['x']} * {location['y']} = {location['x'] * location['y']}"


if __name__ == "__main__":
    print(solution1())
