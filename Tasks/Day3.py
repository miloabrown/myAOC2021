bin_list = []
with open("inputs/input3.txt","r")as t:
    for r in t:
        bin_list.append(r.strip("\n"))
        
#PART1

#Binary to decimal converter bin:str -> ans:int
def bin_to_dec(bin):
    ans = 0
    p = len(bin)-1
    for i in bin:
        ans += int(i)*(2**p)
        p-=1
    return ans
#Function to count the common bit in given index of given list. Returns "1" or "0" :str
def count_common(bins:list,i:int):
    sum = 0
    for num in bins:
        sum+= int(num[i])
    if sum >= round(len(bins)/2):
        return "1"
    else:
        return "0"
#Function uses the count_common function to count the most common bit for each index in given list returns binary number as str
def gamma(bins:list):
    ans = ""
    for x in range(len(bins[0])):
        ans += count_common(bins,x)
        
    return ans
#Converts the bits in given binary number
def epsilon(binary):
    ans = ""
    temp = ""
    for i in binary:
        if i == "1":
            temp = "0"
        else:
            temp = "1"
        ans+=temp
    return ans

gamma_bin = gamma(bin_list)
epsilon_bin = epsilon(gamma_bin)

#Function that goes through binary list recursively and finds our last binary number

def commons(number_list, index):
    ans = ""
    new_list = list(filter(lambda number: number[index] == count_common(number_list,index), number_list))

    if len(new_list) == 1:
        ans = new_list[0]
        print(ans)
    else:
        print(len(new_list))
        commons(new_list,index+1)
    return ans
commons(bin_list,0)
#Test print part1
# print(gamma_bin,epsilon_bin)
# print(bin_to_dec(gamma_bin)*bin_to_dec(epsilon_bin))

#-------------------------------------------#
#PART2
#Oxygen gen (commons) * CO2 scrubber(least commons)

# a = bin_to_dec("011101110101")
# b = bin_to_dec("100100000001")
# # print(keep_commons(bin_list,0))
# # print(keep_uncommons(bin_list,0))


# print(f"{a} * {b} = {a*b}")

#011001101000
#111111001110
#6635440 Too high


#011101110101(common) 1909
#100100000001 2305
#4400245 Too low

#525, 263, 136, 77, 41, 28, 15, 10, 6, 3, 2, 1 -> 011101110101 = 1909
#475, 237, 118, 54, 26, 13, 5, 3, 2, 1 -> 100100000001 = 2305