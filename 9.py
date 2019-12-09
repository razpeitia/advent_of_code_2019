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
            a = int(input("ID > "))
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
            print(a)
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

with open("input09.txt") as f:
    memory = [int(i) for i in f.read().strip().split(",")]

main(memory[:] + [0] * 4000)