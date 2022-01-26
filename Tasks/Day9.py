#Part1 find  all low points in input data
#and count their values together (1 + lowpoint value).
#Sample input should give 15

with open("inputs/sampleinput9.txt","r")as f:
    data = list(map(lambda x: x.strip(),f.readlines()))

#Lets make a matrix and surround it with a layer of 10 on each side
grid = [[10]+[int(num) for num in row]+[10] for row in data]
grid.insert(0,[10 for num in grid[0]])
grid.insert(len(grid),[10 for num in grid[0]])


#Function to check surroundings, --> True if is smaller than all surounding/ False if not
def is_low(x,y):
    point = grid[x][y]
    if grid[x+1][y] > point and grid[x-1][y] > point and grid[x][y+1] > point and grid[x][y-1] > point:
        return True
    else:
        return False

def part1():
    sum = 0
    for x,row in enumerate(grid[1:len(grid)]):
        for y,num in enumerate(row[1:len(row)]):
            if is_low(x,y):
                sum+=(1+grid[x][y])
    print(sum)

part1()
#Part1 answer: 439


#Part2 find three largest basins
#and multiply their sizes together.
#Sample data should give 1134
        