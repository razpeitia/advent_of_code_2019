import time
import math
import numpy as np


def main():
    vfunc = np.vectorize(lambda t: abs(t) % 10)
    with open("input16.txt") as f:
        data = [int(x) for x in f.read().strip()]

    data = np.array(data, np.int64)
    n = len(data)
    x = []
    m = np.array([0, 1, 0, -1], np.int64)
    for i in range(1, n+1):
        y = np.repeat(m, i)
        y = np.tile(y, math.ceil(n / len(y) + 1))
        y = y[1:n+1]
        x.append(y)
    x = np.array(x, np.int64)
    for t in range(100):
        z = vfunc(np.dot(x, data))
        data = z
    print(data[:8])

main()
