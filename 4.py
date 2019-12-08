from itertools import groupby

def is_valid(i):
    s = [int(x) for x in str(i)]
    if not all(s[i+1] >= s[i] for i in range(5)):
        return False
    l = [(k, len(list(v))) for k, v in groupby(s)]
    return len([k for k, v in l if v == 2]) > 0

s = 0
for i in range(137683, 596253 + 1):
    s += is_valid(i)
print(s)