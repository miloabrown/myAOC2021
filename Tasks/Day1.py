with open("inputs/sampleinput1.txt", "r") as f:
    data = [int(x) for x in f]

"""part1"""


def part1():
    return len(list(filter(lambda x: x[0] < x[1], zip(data, data[1:]))))


"""part2"""


def part2():
    return len(list(filter(lambda x: x[0] < x[1], zip(data, data[3:]))))


def main():
    print(f"***Day1***\nPart1: {part1()}\nPart2: {part2()}")


if __name__ == "__main__":
    main()
