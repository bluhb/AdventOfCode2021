from timer import time
import statistics as s
import math as m


def readInput(file):
    with open(file, "r") as f:
        d = [int(x) for x in f.readline().strip().split(",")]
    return d

def calcFuelUsage(end):
    fuel  = 0
    usage = [0]
    for i in range(1,end+1):
        usage.append(usage[i - 1] + i)
    return usage

@time
def solution1(l):
    goal = s.median(l)
    fuel = 0
    for i in l:
        fuel += abs(i - goal)
    print(f"# Solution 1: - Goal: {goal} - Fuel consumption: {fuel}")

@time
def solution2(l):
    goal = (m.ceil(s.mean(l)), m.floor(s.mean(l)))
    fuel = [0,0]
    for x in [0,1]:
        dif = []
        g = goal[x]
        for i in l:
            dif.append(abs(i - g))
        usages = calcFuelUsage(int(max(dif)))
        for i in dif:
            fuel[x] += usages[i]

    print(f"# Solution 2: - Goal: {goal} - Fuel consumption: {fuel}, answer: {min(fuel)}")

data = readInput("input.txt")
solution1(data)
solution2(data)


# Solution 1: - Goal: 372.0 - Fuel consumption: 337488.0
# Function solution1(<class 'list'>,): time elapsed: 0.199 [ms]
# Solution 2: - Goal: (481, 480) - Fuel consumption: [89647716, 89647695], answer: 89647695
# Function solution2(<class 'list'>,): time elapsed: 1.780 [ms]
