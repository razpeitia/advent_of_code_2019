import bisect


def parse_step(step):
    mult, product = step.strip().split()
    return int(mult), product


def parse_steps(steps):
    return [parse_step(step) for step in steps.split(",")]


def resolve(index, need, have):
    while True:
        try:
            product = next(i for i in need if i != 'ORE')
        except StopIteration:
            break
        quantity, steps = index[product]
        d, m = divmod(need[product], quantity)
        need.pop(product, None)
        if m > 0:
            have[product] = quantity - m
            d += 1
        for qty, material in steps:
            need[material] = need.get(material, 0) + d * qty - have.get(material, 0)
            have.pop(material, None)
    return need['ORE']


class Arr:
    def __init__(self, index):
        self.__index = index

    def __len__(self):
        return 10**12

    def __getitem__(self, item):
        return resolve(self.__index, {"FUEL": item}, {})


def main():
    with open("input14.txt") as f:
        index = {}
        for line in f:
            line = line.strip()
            steps, produce = line.split("=>")
            mult, product = parse_step(produce)
            assert product not in index, f"Expected only 1 product {product}"
            index[product] = (int(mult), parse_steps(steps))

    arr = Arr(index)
    fuel = bisect.bisect_left(arr, 10**12)
    ore = resolve(index, {"FUEL": fuel - 1}, {})
    print(fuel - 1, ore)
    ore = resolve(index, {"FUEL": fuel}, {})
    print(fuel, ore)


main()
