import collections
import copy
data = []
with open("inputs/testinput6.txt","r")as f:
    for row in f:
        for value in row.strip().split(","):
            data.append(int(value))

#Part1 answer was 351188

fish = collections.Counter(data)
def fishfarm(days):
    global fish
    for day in range(days):
        new_dict = {}
        new_fish = fish[0] if 0 in fish.keys() else 0
        six = fish[6] if 6 in fish.keys() else False
        for key in fish:
            if key == 0:
                new_dict[6] = (new_fish + fish[7]) if 7 in fish.keys() else new_fish
                new_dict[8] = new_fish
            elif key == 7:
                new_dict[6] = new_fish + fish[7]   
            elif key == 6:
                new_dict[5] = six
            else:
                new_dict[key-1] = fish[key]
        fish = new_dict
    sum = 0
    for key in fish:
        sum+=fish[key]
    print(sum)
                
fishfarm(80)
fishfarm(256)

#Output:
#5934: is correct 
#28671831483421 is WAY too high!
