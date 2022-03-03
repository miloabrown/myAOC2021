from collections import deque

with open("inputs/sampleinput6.txt", "r") as f:
    data = [int(x) for x in f.readline().split(",")]

"""Function for counting the amount of spawned fish in given days"""


def fishfarm(days):
    fish = deque()
    for f in range(9):
        fish.append(data.count(f))
    for _ in range(days):
        fish.rotate(-1)
        fish[6] += fish[8]
    return sum(fish)


def part1():
    return fishfarm(80)


def part2():
    return fishfarm(256)


if __name__ == "__main__":
    print(f"***Day6***\nPart1: {part1()}\nPart2: {part2()}")

# Output:
# Day6:
# Part1: 351188 (sample: 5934)

# Part2: 1595779846729 (sample: 26984457539)
