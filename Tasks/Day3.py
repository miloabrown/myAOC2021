with open("inputs/sampleinput3.txt","r")as f:
    data = [number.strip() for number in f]

'''Functions to find common and uncommon bits for given index'''
def common_bit_for(binaries,index):
    return sorted([x[index] for x in binaries])[int(len(binaries)/2)]

def uncommon_bit_for(binaries,index):
    return str(abs(int(common_bit_for(binaries,index))-1))

'''PART1''' #sample input answer: 198 
def part1():
    epsilon=gamma=""
    index = 0
    while index<len(data[0]):
        gamma+=common_bit_for(data,index)
        epsilon+=uncommon_bit_for(data,index)  
        index+=1
    print("Part1:",int(gamma,2)*int(epsilon,2))
    
'''PART2'''
def part2(): #sample input answer 230
    def oxygen(binaries,index):
        if len(binaries) > 1:
            return oxygen(list(filter(lambda x:x[index] == common_bit_for(binaries,index),binaries)),index+1)
        else:
            return(binaries[0])
    def co(binaries,index):
        if len(binaries) > 1:
            return co(list(filter(lambda x:x[index] == uncommon_bit_for(binaries,index),binaries)),index+1)
        else:
            return(binaries[0])
    print("Part2:",int(oxygen(data,0),2)*int(co(data,0),2))

if __name__ == "__main__":
    print("Day3: ")
    part1()
    part2()