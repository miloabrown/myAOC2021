data = []
with open("inputs/input6.txt","r")as f:
    for row in f:
        for value in row.strip().split(","):
            data.append(int(value))
#We need to go through our input data 
#and decrease each value by 1
#If value == 0, it changes to a 6 and we add a new item
#to the list with a value of 8
#This goes on for 80 days so we need to do it 80 times.
# days1 = 79

#PART1

# def part1(data):
#     global days1
#     temp_data = data.copy()
#     new_data = list(map(lambda x: x+6 if x==0 else x-1, data))
#     for fish in temp_data:
#         if fish == 0:
#             new_data.append(8)
#     if days1 > 0:
#         days1-=1
#         return(part1(new_data))
#     else:
#         return new_data
# ans = part1(data)       
# print(len(ans),"Part1 done!")

#Answer was 351188


#PART2:

#Our code, at the moment, is too slow to determine an answer for part2 in tolerable time so we need to tweak it.
#The recursive method in part1 is probably the most time consuming so let's try a different approach.

def part2():
    global data
    sum=0
    for day in range(80):
        new_fish = data.count(0)
        data = list(map(lambda x: x+6 if x==0 else x-1, data))
        data.extend([8]*new_fish)
        sum+=new_fish
        print(new_fish/80)
    return data
print(len(part2()),"Part2 done!")

