with open("inputs/sampleinput2.txt", "r") as f:
    data = [(x.split(" ")[0], x.split(" ")[1]) for x in f]
    commands = [(x[0], int(x[1].strip())) for x in data]

"""part1"""


def part1():
    x, y = sum(x[1] for x in filter(lambda x: x[0] == "forward", commands)), sum(
        x[1] for x in filter(lambda x: x[0] == "down", commands)
    ) - sum(x[1] for x in filter(lambda x: x[0] == "up", commands))

    return x * y


"""part2"""


def part2():
    x, y, aim = 0, 0, 0
    for command in commands:
        match command[0]:
            case "forward":
                x += command[1]
                y += aim * command[1]
            case "up":
                aim -= command[1]
            case "down":
                aim += command[1]
    return x * y


def main():
    print(f"***Day2***\nPart1: {part1()}\nPart2: {part2()}")


if __name__ == "__main__":
    main()
