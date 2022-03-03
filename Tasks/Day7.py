data = []
with open("inputs/input7.txt", "r") as f:
    for c in sorted(f.read().strip().split(","), key=lambda x: int(x)):
        data.append(int(c))

positions = [*range(min(data), max(data) + 1)]


def part1():
    def count_cost(pos):
        return sum(map(lambda x: abs(x - pos), data))

    return min(map(count_cost, positions))


def part2():
    def cumul_sum(x: int):
        return sum([*range(x + 1)])

    def count_cost(pos):
        return sum(map(lambda x: cumul_sum(abs(x - pos)), data))

    return min(map(count_cost, positions))


def main():
    print(f"***Day7***\nPart1: {part1()}\nPart2: {part2()}")


if __name__ == "__main__":
    main()


# part1: 347449 (Sample: 37)
# part2: 98039527 (Sample: 168)
