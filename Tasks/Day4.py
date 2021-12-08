file = []
boards = []
with open("inputs\input4.txt","r") as t:
    for r in t:
        file.append(r.strip("\n"))
#Remove whitespace from our "file"-list
file = [x for x in file if x]

#numberdraw has the drawn numbers in draw order as a list
numberdraw = file[0].split(",")


#Function to iterate through list in chunks of 5 to get our boards
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))
for board in chunker(file[1:],5):
    boards.append(board)
for board in boards:
    for index,row in enumerate(board):
        board[index] = row.split()
    
# Now we have our bingo number draw as a list and our boards/answer sheets in another list 

# Next we need something to check our boards for numbers 
# also we need to know the location of each number to check for 
# finished rows and columns
# And some method of marking "hits"


#mark_board "marks" given board if the correct number is found. (Replaces with "*")
def mark_board(number,board):
    for row in board:
        for index,c in enumerate(row):
            if c == number and not check_board(board):
                row[index] = "*"

#check_board checks given board for rows or columns of five. Returns True or False
def check_board(board):
    
    def check_row(row):
        if row.count("*") == 5:
            return True
    def check_col(index):
        column = []
        for row in board:
            column.append(row[index])
        return check_row(column)
    for index,row in enumerate(board):
        if check_row(row) or check_col(index):
            return True
        else:
            return False
def count_sum(board):
    sum = 0
    for row in board:
        for c in row:
            if c.isnumeric():
                sum+=int(c)
    return sum


def run():
    last_num = 0
    latest = []
    for number in numberdraw:
        for board in boards:
            mark_board(number,board)
            if check_board(board):
                latest = board
                last_num = number
                # return(int(number)*count_sum(board))
    print(latest,"\n",last_num,"\n",boards.index(latest))
    return(int(number)*count_sum(latest))
                
            
print(run())
print("done")