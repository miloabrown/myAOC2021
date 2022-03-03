import time
dots = []
commands = []
with open("inputs/sampleinput13.txt","r")as f:
    for row in f:
        if row[0].isnumeric():
            dots.append((int(row.strip().split(",")[0]),int(row.strip().split(",")[1])))
        elif row != "\n":
            commands.append((row.strip().split("along ")[1].split("=")[0],int(row.strip().split("along ")[1].split("=")[1])))

#Part1
#Draw dots on board and initiate board.
#Check first command.
#if y: 
#   "move" dots from under the crease_point (dot_y>crease_point) (dot-crease_point)*2 upward
#if x:
#   draw crease with "|"
#   "move" dots on right side of crease_point (dot_x>crease_point) (dot-crease_point*2 left)

#Board dimensions 
height = (max(map(lambda x:x[1],dots))+1)
width = (max(map(lambda x:x[0],dots))+1)
#Initiate board
def draw_dots(d,h,w): #(board, dots, height, width)
    b = [["#" if (x,y) in d else "." for x in range(w)] for y in range(h)]
    return b

#Print board
def print_board(board):
    for i,row in enumerate(board):
        print(i,row)
        
#Count "#" in board
def count_dots(board):
    return sum(map(lambda row: row.count("#"),board))

#Crease function
def crease(cmd,point):
    if cmd == "y":
        h,w = (height-point),width
        new_dots = (list(filter(lambda tup: tup[1]<point,dots)))
        new_dots.extend((list(map(lambda tup: (tup[0],tup[1]-((tup[1]-point)*2)),list(filter(lambda tup: tup[1]>7,dots))))))
    else:
        h,w = height,(width-point)
        new_dots = (list(filter(lambda tup: tup[0]<point,dots)))
        new_dots.extend((list(map(lambda tup: (tup[0]-((tup[0]-point)*2),tup[1]),list(filter(lambda tup: tup[0]>7,dots))))))
        
    return(draw_dots(new_dots,h,w))

def part1():
    timer = time.time()
    board = draw_dots(dots,height,width)
    print(f"Part1: {count_dots(crease(commands[0][0],commands[0][1]))}\nTime: {(time.time() - timer)}")

part1()