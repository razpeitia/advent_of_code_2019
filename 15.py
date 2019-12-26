from collections import deque


def machine(memory, signal):
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
            a = next(signal)
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


def print_grid(grid):
    for row in grid:
        print(''.join(row))
    print()


def signals(grid, state):
    i, j = len(grid) // 2, len(grid[0]) // 2
    grid[i][j] = 'D'
    while True:
        last_move, last_response, history, s, _ = state
        if last_response == 2:
            state[4] = (i, j)
        if state[4] is not None:
            grid[state[4][0]][state[4][1]] = '*'
        if last_move is not None and last_response is not None:
            ni, nj = i, j
            # north (1), south (2), west (3), and east (4)
            if last_move == 1:
                ni -= 1
            elif last_move == 2:
                ni += 1
            elif last_move == 3:
                nj -= 1
            elif last_move == 4:
                nj += 1

            if last_response == 0:
                grid[ni][nj] = '#'
            else:
                if s == "explore":
                    history.append(last_move)
                grid[i][j] = ' '
                i, j = ni, nj
                grid[i][j] = 'D'
        # print_grid(grid)
        x = None
        if grid[i][j+1] == '.':
            x = 4
        elif grid[i][j-1] == '.':
            x = 3
        elif grid[i-1][j] == '.':
            x = 1
        elif grid[i+1][j] == '.':
            x = 2
        if x is None:
            state[3] = "backtrack"
            if not history:
                yield 5
            a = history.pop()
            if a == 1:
                x = 2
            elif a == 2:
                x = 1
            elif a == 3:
                x = 4
            elif a == 4:
                x = 3
        else:
            state[3] = "explore"

        state[0] = x
        yield x

def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'D':
                return (i, j)

def resolve(grid, goal):
    start = find_start(grid)
    q = deque([(1, start)])
    seen = set([start])
    while q:
        c, (i, j) = q.popleft()
        if (i, j) == goal:
            return c
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            if grid[ni][nj] == '#' or (ni, nj) in seen:
                continue
            q.append((c+1, (ni, nj)))
            seen.add((ni, nj))


def resolve2(grid, goal):
    start = find_start(grid)
    i, j = start
    grid[i][j] = ' '
    i, j = goal
    ans = 1
    grid[i][j] = ans
    while True:
        found_space = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == ans:
                    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        ni, nj = i + di, j + dj
                        if grid[ni][nj] == ' ':
                            found_space = True
                            grid[ni][nj] = ans + 1
        if not found_space:
            break
        ans += 1
    return ans


def main():
    grid = [['.'] * 80 for _ in range(50)]
    with open("input15.txt") as f:
        memory = [int(i) for i in f.read().strip().split(",")]

    state = [None, None, [], "explore", None]
    g = machine(memory + [0] * 4000, signals(grid, state))
    while True:
        try:
            state[1] = next(g)
        except StopIteration:
            break
    print_grid(grid)
    print(state[4])
    ans = resolve(grid, state[4])
    print("Part 1 Ans:", ans)

    ans = resolve2(grid, state[4])
    print("Part 2 Ans:", ans)

main()
