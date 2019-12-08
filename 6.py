from collections import deque, defaultdict

g = defaultdict(set)
with open("input06.txt") as f:
    for line in f:
        a, b = line.strip().split(")")
        g[b].add(a)
        g[a].add(b)

def bfs(g, src, dst):
    q = deque([(0, src)])
    v = set()
    while q:
        c, node = q.popleft()
        v.add(node)
        if node == dst:
            print(c - 2)
            return
        for n in g[node]:
            if n not in v:
                q.append((c+1, n))

bfs(g, "YOU", "SAN")