import collections as c

INPUTFILE = "input.txt"

def solution1():
    f = open(INPUTFILE, "r")
    f = f.read().splitlines()
    f = [[x for x in l] for l in f]
    rmc = ""
    rlc = ""
    for i in range(0, len(f[0])):
        d = list(map( lambda y: y[i], f ))
        rmc += str(c.Counter(d).most_common(1)[0][0])
        rlc += "1" if rmc[-1] == "0" else "0"
    rmc_int = int(rmc, 2)
    rlc_int = int(rlc, 2)
    return (
            f"most common: {rmc} -> int: {rmc_int}",
            f"least common: {rlc} -> int: {rlc_int}",
            f"puzzle answer: {rmc_int} * {rlc_int} = {rmc_int * rlc_int}"
        )

def solution2():
    f = open(INPUTFILE, "r")
    f = f.read().splitlines()
    f = [[x for x in l] for l in f]
    mc_l = f
    lc_l = f
    for i in range(0, len(f[0])):
        d = list(map( lambda y: y[i], mc_l ))
        r = c.Counter(d).most_common()
        mc = str(r[0][0] if r[0][1] > r[1][1]  else 1 ) #adjust to 1 if both 0 and 1 have the same occurences
        mc_l = [x for x in mc_l if x[i] == mc]
        if len(mc_l) == 1:
            break
    for i in range(0, len(f[0])):
        d = list(map( lambda y: y[i], lc_l ))
        r = c.Counter(d).most_common()
        lc = str(r[1][0] if r[0][1] > r[1][1]  else 0 ) #adjust to 0 if both 0 and 1 have the same occurences
        lc_l = [x for x in lc_l if x[i] == lc]
        if len(lc_l) == 1:
            break
    if len(mc_l) > 1 or len(lc_l) > 1:
        raise ValueError("we found more than 1 answer")
    rmc = "".join(mc_l[0])
    rmc_int = int(rmc, 2)
    rlc = "".join(lc_l[0])
    rlc_int = int(rlc, 2)

    return (
            f"most common: {rmc} -> int: {rmc_int}",
            f"least common: {rlc} -> int: {rlc_int}",
            f"puzzle answer: {rmc_int} * {rlc_int} = {rmc_int * rlc_int}"
        )

def test():
    x = [[1,2,3,4,5], [10,8,7,6,5]]
    print(x)
    for i in range(0,len(x[0])):
        dirk = list(map( lambda y: y[i], x ))
        print(dirk)

print("solution1")
print(*solution1(), sep="\n")

print("\nsolution2")
print(*solution2(), sep="\n")
