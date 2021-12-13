data = []
with open("inputs/input1.txt","r")as t:
    for r in t:
        data.append(int(r))
#
#part1
#
sum = 0
for i,j in enumerate(data):
    try:
        if j > data[i-1]:
            sum+=1
    except IndexError:
        continue
#
#part2
#
sum=0
for i,j in enumerate(data):
    try:
        a = data[i]
        b = data[i+3]
    except IndexError:
        a = b = 0
    if a < b:
        sum+=1
print(sum)
