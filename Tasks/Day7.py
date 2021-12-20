import collections
import time
data = []
with open("inputs/input7.txt","r")as f:
    for c in sorted(f.read().strip().split(","),key = lambda x: int(x)):
        data.append(int(c))

positions = [*range(min(data),max(data)+1)]

def cumul_sum(x:int):
    return sum([*range(x+1)])

def count_cost1(pos):
    return sum(map(lambda x:abs(x-pos),data))
def count_cost2(pos):
    return sum(map(lambda x:cumul_sum(abs(x-pos)),data))
timer = time.time()
print(f"part1 = {min(map(lambda x: count_cost1(x),positions))}\nTime: {(time.time() - timer)}")
print(f"part2 = {min(map(lambda x: count_cost2(x),positions))}\nTime: {(time.time() - timer)}")

#part1: 347449