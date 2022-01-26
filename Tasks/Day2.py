with open("inputs/input2.txt","r")as f:
    data = [(x.split(" ")[0],x.split(" ")[1]) for x in f]
    commands = [(x[0],int(x[1].strip())) for x in data]

'''part1'''
def part1():
    x,y = sum(x[1]for x in filter(lambda x: x[0] == "forward",commands)),\
          sum(x[1]for x in filter(lambda x: x[0] == "down",commands))-sum(x[1]for x in filter(lambda x: x[0] == "up",commands))
    
    print("part1:",x*y)
    
'''part2'''
def part2():
    x,y = 0,0
    aim = 0
    for command in commands:
        match command[0]:
            case "forward":
                x+=command[1]
                y+= aim*command[1]
            case "up":
                aim-=command[1]
            case "down":
                aim+=command[1]
    print("part2:",x*y)

if __name__ == "__main__":
    print("Day2: ")
    part1() #Sampleinput answer: 150
    part2() #Sampleinput answer: 900