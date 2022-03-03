import numpy as np

with open("inputs/sampleinput5.txt", "r") as f:
    data = [list(map(int, x.strip().replace(" -> ", ",").split(","))) for x in f]


"""find max values to get the needed size for our matrix"""
max_x, max_y = max(map(lambda x: max(x[0], x[2]), data)) + 1, max(
    map(lambda x: max(x[1], x[3]), data)
)

"""Part1"""


def part1():
    """creating a matrix full of zeros"""
    grid = np.zeros((max_x + 1, max_y + 1), dtype=int)
    for line in data:
        x1, y1, x2, y2 = map(int, line)
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[y, x1] += 1
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[y1, x] += 1
    return (grid >= 2).sum()


"""Part2"""


def part2():
    """creating a new matrix full of zeros"""
    grid = np.zeros((max_x + 1, max_y + 1), dtype=int)
    for line in data:
        x1, y1, x2, y2 = map(int, line)
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[y, x1] += 1

        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[y1, x] += 1

        else:
            step_x = 1 if x2 > x1 else -1
            step_y = 1 if y2 > y1 else -1
            for i in range(abs(x1 - x2) + 1):
                new_x = x1 + i * step_x
                new_y = y1 + i * step_y
                grid[new_y, new_x] += 1
    return (grid >= 2).sum()


def main():
    print(f"***Day5***\nPart1: {part1()}\nPart2: {part2()}")


if __name__ == "__main__":
    main()

# part1 1st try, 940539: too high ; 2nd try 8060: Correct!

# part2 1st try, 21662: too high ; 2nd try 21577: Correct!
