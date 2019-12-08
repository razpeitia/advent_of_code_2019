def main(memory, noun, verb):
    memory[1] = noun
    memory[2] = verb
    PC = 0
    while True:
        opcode = memory[PC]
        if opcode == 99:
            break
        elif opcode == 1:
            memory[memory[PC+3]] = memory[memory[PC+1]] + memory[memory[PC+2]]
        elif opcode == 2:
            memory[memory[PC+3]] = memory[memory[PC+1]] * memory[memory[PC+2]]
        PC += 4
    return memory[0]

with open("input02.txt") as f:
    memory = [int(i) for i in f.read().strip().split(",")]

def explore():
    for noun in range(100):
        for verb in range(100):
            if main(memory[:], noun, verb) == 19690720:
                print(noun, verb)
                return
explore()