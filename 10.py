from itertools import combinations

def print_map(M):
    print('\n'.join(''.join(row) for row in M))

def collinear(p0, p1, p2):
    x1, y1 = p1[0] - p0[0], p1[1] - p0[1]
    x2, y2 = p2[0] - p0[0], p2[1] - p0[1]
    return abs(x1 * y2 - x2 * y1) == 0

def point_in_segment(p, s):
    x3, y3 = p
    x1, y1, x2, y2 = s

    crossproduct = (y3 - y1) * (x2 - x1) - (x3 - x1) * (y2 - y1)

    # compare versus epsilon for floating point values, or != 0 if using integers
    if abs(crossproduct) > 0.0:
        return False

    dotproduct = (x3 - x1) * (x2 - x1) + (y3 - y1) * (y2 - y1)
    if dotproduct < 0:
        return False

    squaredlengthba = (x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1)
    if dotproduct > squaredlengthba:
        return False
    return True

def count(asteroids, asteroid):
    visited = set()
    def distance(p):
        x1, y1 = p
        x2, y2 = asteroid
        return ((x1 - x2) ** 2) + ((y1 - y2) ** 2)

    c = 0
    for a in sorted([x for x in asteroids if x != asteroid], key=distance):
        if a in visited: continue
        visited.add(a)
        for b in (x for x in asteroids if (x != a) and (x != asteroid)):
            if collinear(asteroid, a, b) and point_in_segment(a, asteroid + b):
                visited.add(b)
        c += 1
    return c

def main():
    with open("input10.txt") as f:
        M = [list(line.strip()) for line in f]
    m = len(M)
    n = len(M[0])
    asteroids = [(i, j) for i in range(m) for j in range(n) if M[i][j] == '#']
    ans = {}
    for asteroid in asteroids:
        ans[asteroid] = count(asteroids, asteroid)
    best = max(ans, key=lambda x: ans[x])
    print(best[::-1], ans[best])


main()