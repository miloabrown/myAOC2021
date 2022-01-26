from unicodedata import name


with open("inputs/input1.txt","r")as f:
    data = [int(x) for x in f]

'''part1'''
def part1():
    print("Part1:",len(list(filter(lambda x: x[0]<x[1],zip(data,data[1:])))))
    
'''part2'''        
def part2():
    print("Part2:",len(list(filter(lambda x: x[0]<x[1],zip(data,data[3:])))))
    
if __name__ == "__main__":
    part1()
    part2()