input = []
with open("inputs/input5.txt","r")as f:
    for row in f:
        input.append(row)

# Make two lists, one for our starting coordinates, the other for our endpoint coordinates
startpoints = []
endpoints = []
for row in input:
    startpoints.append(row.split(" -> ")[0])
    endpoints.append(row.split(" -> ")[1].strip())
   
# Lets make a matrix to mark our pipelines. It needs to be as wide 
# as the biggest "y"-coordinate and as long as the biggest "x" coordinate

# Function to find the biggest x and y and returns them as tuple (x,y)
def biggest(start_list:list,end_list:list) -> tuple():
    s_list = start_list.copy()
    s_list.extend(end_list)
    big_x = 0
    big_y = 0
    for i in s_list:
        x = i.split(",")[0]
        y = i.split(",")[1]
        if int(x) > big_x:
            big_x = int(x)
        if int(y) > big_y:
            big_y = int(y)
    return (big_x,big_y)
x,y = biggest(startpoints,endpoints)

row = [0]*(y+2)
pipelines = []
for i in range(x+2):
    pipelines.append(row.copy())

# Now we have a matrix in size X x Y filled with zeros.
# Now we need a function to go through our pipelines and "draw" them in our pipelines- matrix.

def draw_pipes()-> list:    
#Function to draw horizontal lines:
    def draw_h(y,x1,x2):
        for a in range(x1,x2+1): 
            pipelines[y][a]+=1    
#Function to draw vertical lines:
    def draw_v(x,y1,y2):
        for a in range(y1,y2+1):
            pipelines[a][x]+=1
#Function to draw diagonal lines: 
    def draw_d(x1,x2,y1,xdir,ydir): #8,0,0,-1,1
        x = x1 #8
        y = y1 #0
        for a in range(abs(x2-x1)+1):
            pipelines[y][x]+=1
            x+=xdir
            y+=ydir
      
    for index, i in enumerate(startpoints):
        x_start = int(i.split(",")[0])
        y_start = int(i.split(",")[1])
        x_end = int(endpoints[index].split(",")[0])
        y_end = int(endpoints[index].split(",")[1])

#Going through the diagonal posibilities
        if x_start != x_end and y_start != y_end:
            if x_start < x_end and y_start < y_end:
                draw_d(x_start,x_end,y_start,1,1)
            if x_start < x_end and y_start > y_end:
                draw_d(x_start,x_end,y_start,1,-1) 
            if x_start > x_end and y_start < y_end:
                draw_d(x_start,x_end,y_start,-1,1)
            if x_start > x_end and y_start > y_end:
                draw_d(x_start,x_end,y_start,-1,-1)
#And horizontal, vertical posibilities          
        elif x_start == x_end and y_start < y_end:
            draw_v(x_start,y_start,y_end)
        elif x_start == x_end and y_start > y_end:
            draw_v(x_start,y_end,y_start)   
        elif y_start == y_end and x_start < x_end:
            draw_h(y_start,x_start,x_end)
        elif y_start == y_end and x_start > x_end:
            draw_h(y_start,x_end,x_start)
        
#Function to count where two or more pipelines overlap:
def count_overlaps():
    sum = 0
    for x in pipelines:
        for y in x:
            if y >=2:
                sum+=1
    return sum

#Running our functions to get answer
draw_pipes()
ans = count_overlaps()
print(ans) 

#part1 1st try, 940539: too high ; 2nd try 8060: Correct!

#part2 1st try, 21662: too high ; 2nd try 21577: Correct!