def main():
    with open("input16.txt") as f:
        data = [int(x) for x in f.read().strip()]
    data = data * 10000
    n = len(data)
    offset = int(''.join(map(str, data[:7])))
    print("offset", offset)

    for t in range(100):
        output = [0] * n
        s = 0
        for i in range(n-1, n // 2, -1):
            s += data[i]
            output[i] = s % 10
        x = output[offset:offset+8]
        x = ''.join(map(str, x))
        print(f"{t+1} -> {x}")
        data = output

main()
