def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def segments(cable):
    x, y = 0, 0
    ans = []
    for c in cable:
        d = c[0]
        l = int(c[1:])
        s = [x, y]
        if d == 'R':
            x += l
        elif d == 'U':
            y += l
        elif d == 'D':
            y -= l
        elif d == 'L':
            x -= l
        s += [x, y]
        ans.append(s)
    return ans

def intersect(s1, s2):
    (x1, y1, x2, y2) = s1
    (x3, y3, x4, y4) = s2
    s1_x = x2 - x1
    s1_y = y2 - y1
    s2_x = x4 - x3
    s2_y = y4 - y3
    
    d = (-s2_x * s1_y + s1_x * s2_y)
    if d == 0:
        return False

    s = (-s1_y * (x1 - x3) + s1_x * (y1 - y3)) / d
    t = ( s2_x * (y1 - y3) - s2_y * (x1 - x3)) / d
    if (s >= 0 and s <= 1) and (t >= 0 and t <= 1):
        return (x1 + (t * s1_x), y1 + (t * s1_y))

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

def steps(p, s):
    ans = 0
    for seg in s:
        if point_in_segment(p, seg):
            ans += distance((seg[0], seg[1]), p)
            return ans
        else:
            ans += distance((seg[0], seg[1]), (seg[2], seg[3]))
    assert False, "p={} s={}".format(p, s)

def main():
    with open("input03.txt") as f:
        s1 = segments(next(f).strip().split(","))
        s2 = segments(next(f).strip().split(","))
    ans = None
    for i in s1:
        for j in s2:
            x = intersect(i, j)
            if x:
                if x[0] == 0.0 and x[1] == 0.0:
                    continue
                d1 = steps(x, s1) + steps(x, s2)
                if ans is None:
                    ans = d1
                elif d1 < ans:
                    ans = d1
    print(ans)

main()