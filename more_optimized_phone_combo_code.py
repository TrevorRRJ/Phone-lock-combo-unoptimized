from itertools import permutations #this is for generating the possible sequences
from math import factorial
from time import time

incorrect_pos = 0
#this is where the combinations that are impossible will be tallied

points = ["A", "B", "C", "D", "E", "F", "G", "H", "I"] #each letter represents one dot on the pattern grid with A being upper left, B being upper center, etc. 

incorrect_pattern_pieces = [["A","I","E"], ["A","G","D"], ["A","C","B",], ["B","H","E"], ["C","G","E"], ["C","I","F"], ["D","F","E"], ["G","I","H"]] #for each sub-list if the first and second points are next to eachother before the third point, then the pattern is incorrect

valid = False
while valid == False:
    chain_len = input("How many dots are used?")
    if (str(chain_len).isdigit() == True) and ((int(chain_len) <= 9) and (int(chain_len) >= 2)):
        valid = True
    else:
        print("Please type a valid integer between 2 and 9")
#this ensures that the desired pattern length is valid

time_1 = time()

combos = []
combos_gen = permutations(points, int(chain_len)) #this generates the pattern possibilities
for combo in combos_gen:
    combos.append(list(combo))
#converts tuples to lists so that they can be appended

for patterns in combos:
    n = 0
    done = False
    while (done == False) and (n != 8):
        piece = incorrect_pattern_pieces[n]
        if (piece[2] not in patterns) and (piece[0] in patterns) and (piece[1] in patterns):
            if ((patterns.index(piece[0]) + 1 == patterns.index(piece[1])) or (patterns.index(piece[0]) - 1 == patterns.index(piece[1]))):
                incorrect_pos += 1
                done = True
            else:
                n += 1
        elif ((piece[2] in patterns) and (piece[0] in patterns) and (piece[1] in patterns)): 
            if ((patterns.index(piece[0]) < patterns.index(piece[2])) and (patterns.index(piece[1]) < patterns.index(piece[2])) and ((patterns.index(piece[0]) + 1 == patterns.index(piece[1])) or (patterns.index(piece[0]) - 1 == patterns.index(piece[1])))):
                incorrect_pos += 1
                done = True
            else:
                n += 1
        else:
            n += 1   
#this checks whether or not a pattern is possible

print ((factorial(9) / factorial(9 - int(chain_len))) - incorrect_pos)
time_2 = time()
print (time_2 - time_1)       