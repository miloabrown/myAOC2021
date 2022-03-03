from numpy import prod

with open("inputs/input9.txt", "r") as f:
    data = list(map(lambda x: x.strip(), f.readlines()))


grid = [[9] + [int(num) for num in row] + [9] for row in data]
grid.insert(0, [9 for num in grid[0]])
grid.insert(len(grid), [9 for num in grid[0]])


# Function to check surroundings, --> True if is smaller than all surounding/ False if not
def is_low(x, y):
    point = grid[x][y]
    return (
        grid[x + 1][y] > point
        and grid[x - 1][y] > point
        and grid[x][y + 1] > point
        and grid[x][y - 1] > point
    )


def calculate_basin(x, y, basin):
    basin.append((x, y))
    steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for step in steps:
        new_x, new_y = x + step[0], y + step[1]
        if (new_x, new_y) not in basin and grid[x][y] < grid[new_x][new_y] < 9:
            calculate_basin(new_x, new_y, basin)
    return len(basin)


def part1():
    sum = 0
    for x, row in enumerate(grid[1 : len(grid)]):
        for y, _ in enumerate(row[1 : len(row)]):
            if is_low(x, y):
                sum += 1 + grid[x][y]
    return sum


def part2():
    basins = []
    for x, row in enumerate(grid[1 : len(grid)]):
        for y, _ in enumerate(row[1 : len(row)]):
            if is_low(x, y):
                basins.append(calculate_basin(x, y, []))
    return prod(sorted(basins, reverse=True)[:3])


def main():
    print(f"***Day9***\nPart1: {part1()}\nPart2: {part2()}")


if __name__ == "__main__":
    main()
# Part1 answer: 439 (Sample: 15)
# Part2 answer: 900900 (Sample: 1134)
