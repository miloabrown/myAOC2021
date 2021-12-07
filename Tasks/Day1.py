lista = []
with open("inputs/input1.txt","r")as t:
    for r in t:
        lista.append(int(r))
#
#part1
#
sum = 0
for i,j in enumerate(lista):
    try:
        if j > lista[i-1]:
            sum+=1
    except IndexError:
        continue
#
#part2
#
sum=0
for i,j in enumerate(lista):
    try:
        a = lista[i]+lista[i+1]+lista[i+2]
        b = lista[i+1]+lista[i+2]+lista[i+3]
    except IndexError:
        a = b = 0
    if a < b:
        sum+=1
print(sum)
