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


def main():
    with open("input14.txt") as f:
        index = {}
        for line in f:
            line = line.strip()
            steps, produce = line.split("=>")
            mult, product = parse_step(produce)
            assert product not in index, f"Expected only 1 product {product}"
            index[product] = (int(mult), parse_steps(steps))
    ans = resolve(index, {"FUEL": 1}, {})
    print(ans)


main()
