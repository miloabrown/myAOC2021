commands = []
values = []
with open("inputs/input2.txt","r")as t:
    for r in t:
        commands.append(r.split(" ")[0])
        values.append(int(r.split(" ")[1]))
hor = 0
dep = 0
aim = 0
for i,j in enumerate(commands):
    if j == "forward":
        hor += values[i]
        dep += aim*values[i]
    if j == "down":
        aim += values[i]
    if j == "up":
        aim -= values[i]
print(hor,dep,hor*dep)