def print_map(M, direction, pos):
    for i, row in enumerate(M):
        for j, c in enumerate(row):
            if pos == (i, j):
                print(direction, end='')
            else:
                print(c, end='')
        print()
    print()

def main(memory):
    PC = 0
    RB = 0
    while True:
        opcode = memory[PC]
        mode = ((opcode // 100) % 10), ((opcode // 1000) % 10), ((opcode // 10000) % 10)
        opcode = opcode % 100
        assert mode[2] != 1, "Wrong assuption"
        if opcode == 99:
            break
        elif opcode == 1:
            a = memory[memory[PC+1]] if mode[0] == 0 else memory[PC+1]
            a = memory[a + RB] if mode[0] == 2 else a
            b = memory[memory[PC+2]] if mode[1] == 0 else memory[PC+2]
            b = memory[b + RB] if mode[1] == 2 else b
            addr = memory[PC+3] + (RB if mode[2] == 2 else 0)
            memory[addr] = a + b
            PC += 4
        elif opcode == 2:
            a = memory[memory[PC+1]] if mode[0] == 0 else memory[PC+1]
            a = memory[a + RB] if mode[0] == 2 else a
            b = memory[memory[PC+2]] if mode[1] == 0 else memory[PC+2]
            b = memory[b + RB] if mode[1] == 2 else b
            addr = memory[PC+3] + (RB if mode[2] == 2 else 0)
            memory[addr] = a * b
            PC += 4
        elif opcode == 3:
            a = yield
            if mode[0] == 0:
                memory[memory[PC+1]] = a
            elif mode[0] == 1:
                memory[PC+1] = a
            elif mode[0] == 2:
                memory[RB + memory[PC+1]] = a
            PC += 2
        elif opcode == 4:
            a = memory[memory[PC+1]] if mode[0] == 0 else memory[PC+1]
            a = memory[a + RB] if mode[0] == 2 else a
            yield a
            PC += 2
        elif opcode == 5:
            a = memory[memory[PC+1]] if mode[0] == 0 else memory[PC+1]
            a = memory[a + RB] if mode[0] == 2 else a
            b = memory[memory[PC+2]] if mode[1] == 0 else memory[PC+2]
            b = memory[b + RB] if mode[1] == 2 else b
            if a != 0:
                PC = b
            else:
                PC += 3
        elif opcode == 6:
            a = memory[memory[PC+1]] if mode[0] == 0 else memory[PC+1]
            a = memory[a + RB] if mode[0] == 2 else a
            b = memory[memory[PC+2]] if mode[1] == 0 else memory[PC+2]
            b = memory[b + RB] if mode[1] == 2 else b
            if a == 0:
                PC = b
            else:
                PC += 3
        elif opcode == 7:
            a = memory[memory[PC+1]] if mode[0] == 0 else memory[PC+1]
            a = memory[a + RB] if mode[0] == 2 else a
            b = memory[memory[PC+2]] if mode[1] == 0 else memory[PC+2]
            b = memory[b + RB] if mode[1] == 2 else b

            addr = memory[PC+3] + (RB if mode[2] == 2 else 0)
            memory[addr] = int(a < b)
            PC += 4
        elif opcode == 8:
            a = memory[memory[PC+1]] if mode[0] == 0 else memory[PC+1]
            a = memory[a + RB] if mode[0] == 2 else a
            b = memory[memory[PC+2]] if mode[1] == 0 else memory[PC+2]
            b = memory[b + RB] if mode[1] == 2 else b

            addr = memory[PC+3] + (RB if mode[2] == 2 else 0)
            memory[addr] = int(a == b)
            PC += 4
        elif opcode == 9:
            if mode[0] == 0:
                a = memory[memory[PC+1]]
            elif mode[0] == 1:
                a = memory[PC+1]
            elif mode[0] == 2:
                a = memory[RB + memory[PC+1]]
            RB += a
            PC += 2

with open("input11.txt") as f:
    memory = [int(i) for i in f.read().strip().split(",")]

p = main(memory[:] + [0] * 10000)
UP, DOWN, LEFT, RIGHT = 'UP', 'DOWN', 'LEFT', 'RIGHT'
def get_arrow(direction):
    if direction == UP:
        return '^'
    elif direction == DOWN:
        return 'v'
    elif direction == LEFT:
        return '<'
    elif direction == RIGHT:
        return '>'

def turn(direction, left):
    if not left:
        if direction == UP:
            return RIGHT
        elif direction == RIGHT:
            return DOWN
        elif direction == DOWN:
            return LEFT
        elif direction == LEFT:
            return UP
    else:
        if direction == UP:
            return LEFT
        elif direction == LEFT:
            return DOWN
        elif direction == DOWN:
            return RIGHT
        elif direction == RIGHT:
            return UP

def forward(pos, direction):
    (i, j) = pos
    if direction == UP:
        i -= 1
    elif direction == DOWN:
        i += 1
    elif direction == RIGHT:
        j += 1
    elif direction == LEFT:
        j -= 1
    return (i, j)

direction = UP
W = 100
pos = (W // 2, W // 2)
M = [['#'] * W for _ in range(W)]

s = set()
while True:
    try:
        #print_map(M, get_arrow(direction), pos)
        next(p) # The yield input
        (i, j) = pos
        c = p.send(int(M[i][j] == '#')) # first yield output
        d = next(p) # second yield output
        #print(c, d)
        # I don't thing that -j makes any sense but at least it worked
        if c == 1:
            M[i][-j] = '#'
        else:
            M[i][-j] = '.'
        s.add((i, j))
        direction = turn(direction, d)
        pos = forward(pos, direction)
        #input()
    except StopIteration:
        break
print_map(M, get_arrow(direction), pos)
print(len(s))