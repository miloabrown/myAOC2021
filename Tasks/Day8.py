outputs = []
sig_patterns = []
with open("inputs/input8.txt","r")as f:
    for row in f:
        outputs.append(row.strip().split(" | ")[1].split(" "))
        sig_patterns.append(row.strip().split(" | ")[0].split(" "))
def count_easy_digits(row):
    return sum(map(lambda x: 1 if str(len(x)) in "2347" else 0,row))
# print(f"Part1: {sum(map(lambda x: count_easy_digits(x),outputs))}")
#Part2

#All numbers:
#0: top, bottom, top_left, bottom_left, top_right, bottom_right len 6
#1: top and bottom_right; len 2
#2: top, middle, bottom, top_right, bottom_left; len 5
#3: top, middle, bottom, top_ and bottom_right; len 5
#4: top_left, middle, top_ and bottom_right; len 4
#5: top, middle, bottom, top_left, bottom_right; len 5
#6: top, middle, bottom, top_left, bottom_left, bottom_right; len 6
#7: top, top_right, bottom_right; len 3
#8: all sections; len 7
#9: top, middle, bottom, top_left, top_right, bottom_right len 6

#Digits in length:
#7: 8
#6: 0, 6, 9
#5: 2, 3, 5
#4: 4
#3: 7
#2: 1

#Deduction for each section:
#top: 7-1
#middle: 8-0
#bottom: 9-(4+7)
#bottom_left: 8-9
#top_left: 9-3
#bottom_right: 
#top_right: 8-6

#Sections:
#1/a = top
#2/b = top_left
#3/c = top_right
#4/d = middle
#5/e = bottom_left
#6/f = bottom_right
#7/g = bottom

#Calculate digits:
#1 len:2
#2 8 - (top_left+bottom_right)
#3 8 - (top_left+bottom_left)
#4 len:4
#5 6 - bottom_left
#6 8 - top_right
#7 len:3
#8 len:7
#9 8 - bottom_left
#0 8 - middle

#Fucntion to subtract digit from another. --> Letter(s)
def sub(digit1,digit2):
     return "".join(list(filter(lambda x: x not in digit2,digit1)))
#Function to connect two digits. --> Letters
def add(digit1,digit2):
    return digit1+digit2

#Function to check if given sub_pattern (letters) is in given pattern --> True/False
def is_in(subpat,pat):
    for l in subpat:
        if l not in pat:
            return False
    return True 

#function to get all digits in first 10 signalpatterns
def find_pattern(pattern):
    digits = {}
    sections = {}
    digits[1] = list(filter(lambda x:len(x) == 2,pattern))[0]
    pattern.remove(digits[1])
    
    digits[4] = list(filter(lambda x:len(x) == 4,pattern))[0]
    pattern.remove(digits[4])
    
    digits[7] = list(filter(lambda x:len(x) == 3,pattern))[0]
    pattern.remove(digits[7])
    
    digits[8] = list(filter(lambda x:len(x) == 7,pattern))[0]
    pattern.remove(digits[8])
    
    digits[6] = list(filter(lambda x: is_in(add(sub(digits[4],digits[1]),sub(sub(digits[8],digits[4]),digits[7])),x),pattern))[0]
    pattern.remove(digits[6])
    
    digits[5] = list(filter(lambda x: is_in(x,digits[6]),pattern))[0]
    pattern.remove(digits[5])
    
    digits[9] = list(filter(lambda x: is_in(sub(digits[8],sub(digits[6],digits[5])),x),pattern))[0]
    pattern.remove(digits[9])
    
    digits[0] = list(filter(lambda x:len(x) == 6,pattern))[0]
    pattern.remove(digits[0])
    
    digits[3] = list(filter(lambda x: is_in(sub(digits[1],sub(digits[8],digits[6])),x),pattern))[0]
    pattern.remove(digits[3])
    
    digits[2] = pattern[0]
    pattern.remove(digits[2])
    
    return(digits)


#Function goes through every row and adds the "digit_map" of said row to a list 
digit_maps = []
def maps():
    for row in sig_patterns:
        digit_maps.append(find_pattern(row))

maps()
sum = 0
for index,i in enumerate(digit_maps):
    ans = ""
    # print(f"{index}:{i}")
    for op in outputs[index]:
        for num in i:
            if is_in(op,i[num]) and len(op) == len(i[num]):
                ans+=str(num)
    # print(ans)
    sum+=int(ans)
print(sum)