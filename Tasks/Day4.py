from itertools import chain

with open("inputs\sampleinput4.txt", "r") as f:
    drawpile = f.readline().strip().split(",")
    data = f.read().split()
    boards = [
        [board[index : index + 5] for index in range(0, len(board), 5)]
        for board in [data[x : x + 25] for x in range(0, len(data), 25)]
    ]


def mark_board(number, board):
    for row in board:
        for index, c in enumerate(row):
            row[index] = "*" if (c == number and not check_board(board)) else row[index]


def check_board(board):
    def check_row(row):
        return row.count("*") == 5

    def check_col(index):
        return check_row([row[index] for row in board])

    for index, row in enumerate(board):
        if check_row(row) or check_col(index):
            return True


def count_sum(board):
    return sum(
        map(
            lambda x: int(x),
            filter(lambda x: x.isnumeric(), chain.from_iterable(board)),
        )
    )


def main():
    won = []
    for number in drawpile:
        for index, board in enumerate(boards):
            if index not in won:
                mark_board(number, board)
            if check_board(board) and index not in won:
                won.append(index)
                print(
                    f"Number: {number}\nBoard: {board}\nAnswer:{int(number) * count_sum(board)}"
                )


if __name__ == "__main__":
    main()

# Part1 sample input answer: 188 * 24 = 4512
# Part2 sample input answer: 148 * 13 = 1924
