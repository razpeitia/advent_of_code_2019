def main(memory):
    PC = 0
    while True:
        opcode = memory[PC]
        mode = ((opcode // 100) % 10), ((opcode // 1000) % 10), ((opcode // 10000) % 10)
        opcode = opcode % 100
        assert mode[2] != 1, "Wrong assuption"
        if opcode == 99:
            break
        elif opcode == 1:
            a = memory[memory[PC+1]] if mode[0] == 0 else memory[PC+1]
            b = memory[memory[PC+2]] if mode[1] == 0 else memory[PC+2]
            memory[memory[PC+3]] = a + b
            PC += 4
        elif opcode == 2:
            a = memory[memory[PC+1]] if mode[0] == 0 else memory[PC+1]
            b = memory[memory[PC+2]] if mode[1] == 0 else memory[PC+2]
            memory[memory[PC+3]] = a * b
            PC += 4
        elif opcode == 3:
            a = int(input("ID > "))
            if mode[0] == 0:
                memory[memory[PC+1]] = a
            else:
                memory[PC+1] = a
            PC += 2
        elif opcode == 4:
            a = memory[memory[PC+1]] if mode[0] == 0 else memory[PC+1]
            print(a)
            PC += 2
        elif opcode == 5:
            a = memory[memory[PC+1]] if mode[0] == 0 else memory[PC+1]
            b = memory[memory[PC+2]] if mode[1] == 0 else memory[PC+2]
            if a != 0:
                PC = b
            else:
                PC += 3
        elif opcode == 6:
            a = memory[memory[PC+1]] if mode[0] == 0 else memory[PC+1]
            b = memory[memory[PC+2]] if mode[1] == 0 else memory[PC+2]
            if a == 0:
                PC = b
            else:
                PC += 3
        elif opcode == 7:
            a = memory[memory[PC+1]] if mode[0] == 0 else memory[PC+1]
            b = memory[memory[PC+2]] if mode[1] == 0 else memory[PC+2]
            memory[memory[PC+3]] = int(a < b)
            PC += 4
        elif opcode == 8:
            a = memory[memory[PC+1]] if mode[0] == 0 else memory[PC+1]
            b = memory[memory[PC+2]] if mode[1] == 0 else memory[PC+2]
            memory[memory[PC+3]] = int(a == b)
            PC += 4
    return memory[0]

with open("input05.txt") as f:
    memory = [int(i) for i in f.read().strip().split(",")]

main(memory[:])