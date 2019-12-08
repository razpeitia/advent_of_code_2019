from functools import reduce
with open("input08.txt") as f:
    data = f.read().strip()

m = 6
n = 25

layers = []
it = iter(data)

ln = len(data) // (m * n)
for _ in range(ln):
    layer = [[None] * n for i in range(m)]
    layers.append(layer)
    for i in range(m):
        for j in range(n):
            layer[i][j] = next(it)

def merge(l1, l2):
    layer = [[None] * n for i in range(m)]
    d = {
        ('0', '0'): '0',
        ('0', '1'): '0',
        ('0', '2'): '0',

        ('1', '0'): '1',
        ('1', '1'): '1',
        ('1', '2'): '1',

        ('2', '0'): '0',
        ('2', '1'): '1',
        ('2', '2'): '2',
    }
    for i in range(m):
        for j in range(n):
            a = l1[i][j]
            b = l2[i][j]
            layer[i][j] = d[a, b]
    return layer

img = reduce(merge, layers)
print('\n'.join(''.join(c.replace('0', ' ') for c in row) for row in img))