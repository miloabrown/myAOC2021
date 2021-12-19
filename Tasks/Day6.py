#Read input into "data"-list
import collections
data = []
with open("inputs/input6.txt","r")as f:
    for row in f:
        for value in row.strip().split(","):
            data.append(int(value))
#Function for counting the amount of spawned fish in given days
def fishfarm(days):
    fish = collections.deque()
    for f in range(9):
        fish.append(data.count(f))
    for day in range(days):
        new_fish = fish.copy()[0]
        fish.rotate(-1)
        fish[6] += new_fish
    return(sum(fish))  
                
print(f"Part1: {fishfarm(80)}")
print(f"Part2: {fishfarm(256)}")

#Output:
#Part1: 351188 
# (is correct) 

#Part2: 1595779846729 
# (is correct)
