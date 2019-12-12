from itertools import combinations
from copy import copy
from math import gcd

def calc(x1, x2):
    if x1 > x2:
        return (-1, 1)
    elif x1 < x2:
        return (1, -1)
    else:
        return (0, 0)

def print_all(i, moons, speeds):
    print("After {} steps:".format(i))
    ans = 0
    for moon in moons:
        print("({}) pos=<x={:>4}, y={:>4}, z={:>4}>, vel=<x={:>4}, y={:>4}, z={:>4}>".format(*(moon + speeds[moon[0]])))
        _, x, y, z = moon
        vx, vy, vz = speeds[moon[0]]
        pot = abs(x) + abs(y) + abs(z)
        kin = abs(vx) + abs(vy) + abs(vz)
        ans += (kin * pot)
    print("ans={}".format(ans))
    print()

def main():
    with open("input12.txt") as f:
        table = str.maketrans(dict.fromkeys("<>=xyz "))
        moons = [[a for a in line.strip().translate(table).split(",")] for line in f]
        moons = [[i, int(x), int(y), int(z)] for (i, (x, y, z)) in enumerate(moons, start=0)]
    speeds = [[0] * 3 for _ in moons]
    i = 0
    T1 = [moon[1] for moon in moons]
    T2 = [moon[2] for moon in moons]
    T3 = [moon[3] for moon in moons]
    T4 = [0 for _ in moons]
    X = [0] * 3
    while True:
        #print_all(i, moons, speeds)
        for (id1, x1, y1, z1), (id2, x2, y2, z2) in combinations(moons, 2):
            d1, d2 = calc(x1, x2)
            speeds[id1][0] += d1
            speeds[id2][0] += d2
            d1, d2 = calc(y1, y2)
            speeds[id1][1] += d1
            speeds[id2][1] += d2
            d1, d2 = calc(z1, z2)
            speeds[id1][2] += d1
            speeds[id2][2] += d2
        moons = [[id, x+speeds[id][0], y+speeds[id][1], z+speeds[id][2]] for (id, x, y, z) in moons]
        
        t1 = [moon[1] for moon in moons]
        t2 = [moon[2] for moon in moons]
        t3 = [moon[3] for moon in moons]
        t4 = [speed[0] for speed in speeds]
        t5 = [speed[1] for speed in speeds]
        t6 = [speed[2] for speed in speeds]
        
        if X[0] == 0 and t1 == T1 and t4 == T4:
            X[0] = i+1
            print("x=", i+1)
        if X[1] == 0 and t2 == T2 and t5 == T4:
            X[1] = i+1
            print("y=", i+1)
        if X[2] == 0 and t3 == T3 and t6 == T4:
            X[2] = i+1
            print("z=", i+1)
        i += 1
        if all(X):
            break
        #input("Press enter...")
    print(X)
    lcm = X[0]
    for i in X[1:]:
      lcm = lcm*i//gcd(lcm, i)
    print(lcm)

main()