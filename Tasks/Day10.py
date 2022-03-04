with open("inputs/input10.txt", "r") as f:
    data = [line.strip() for line in f]

symbols = {"(": ")", "[": "]", "{": "}", "<": ">"}

scores1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
scores2 = {")": 1, "]": 2, "}": 3, ">": 4}


def find_corrupt_symbols(input):
    """function to find first corrupt symbol in each corrupt row. Also returns a list of incomplete rows for part2"""
    corrupt_symbols = []
    corrupt_rows = []
    for row in input:
        opens = [row[0]]
        latest_open = row[0]
        for symbol in row:
            if symbol in symbols.keys():
                opens.append(symbol)
                latest_open = symbol
            elif symbol == symbols[latest_open]:
                opens.pop()
                latest_open = opens[-1]
            else:
                corrupt_symbols.append(symbol)
                corrupt_rows.append(row)
                break

    incomplete_rows = [x for x in input if x not in corrupt_rows]
    return (corrupt_symbols, incomplete_rows)


def complete_rows(input):
    """function completes the rows in input and returns a list of completion rows"""
    completions = []
    for row in input:
        opens = ""
        for symbol in row:
            if symbol in symbols.keys():
                opens += symbol
            elif symbol == symbols[opens[-1]]:
                opens = opens[:-1]
        completions.append(list(map(lambda x: symbols[x], opens))[::-1])
    return completions


def calculate_part2(row):
    """calculates the score for "completion-row" """
    total = 0
    for item in row:
        total = (total * 5) + scores2[item]
    return total


def part1():
    return sum(map(lambda x: scores1[x], find_corrupt_symbols(data)[0]))


def part2():
    incomplete = find_corrupt_symbols(data)[1]
    scores_list = sorted(list(map(calculate_part2, complete_rows(incomplete))))
    return scores_list[int(len(scores_list) / 2)]


def main():
    print(f"***Day10***\nPart1: {part1()}\nPart2: {part2()}")


if __name__ == "__main__":
    main()


# Part1 answer:344193 (Sample: 26397)
# Part2 answer:3241238967 (Sample: 288957)
