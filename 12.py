from itertools import combinations
from copy import copy

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
    for i in range(1000+1):
        print_all(i, moons, speeds)
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
        #input("Press enter...")

main()