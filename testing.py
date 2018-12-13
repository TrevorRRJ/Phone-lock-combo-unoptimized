
correct_possibilities = 0
incorrect_possibilities = 0
total_possibilities = 0
points = {"A":0, "B":0, "C":0, "D":0, "E":0, "F":0, "G":0, "H":0, "I":0,}
values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
valid = False
len1 = 10
len2 = 10
len3 = 10
len4 = 10
len5 = 10 
len6 = 10
len7 = 10
len8 = 10

while valid == False:
    chain_len = input("How many dots are used?")
    if (str(chain_len).isdigit() == True) and ((int(chain_len) <= 9) and (int(chain_len) >= 2)):
        valid = True
    else:
        print("Please type a valid integer between 2 and 9")

if int(chain_len) < 8:
    len8 = 8
    
if int(chain_len) < 7:
    len7 = 7

if int(chain_len) < 6:
    len6 = 6

if int(chain_len) < 5:
    len5 = 5

if int(chain_len) < 4:
    len4 = 4

if int(chain_len) < 3:
    len3 = 3

if int(chain_len) == 2:
    len2 = 2

for x in values:
        points["A"] = x
        for y in values:
            if y != x:
                points["B"] = y
                for z in values:
                    if z != y and z !=x:
                        points["C"] = z
                        for l in values:
                            if l != y and l !=x and l != z:
                                points["D"] = l
                                for m in values:
                                    if m != y and m !=x and m != z and m != l:
                                        points["E"] = m
                                        for o in values:
                                            if o != y and o !=x and o != z and o != l and o !=m:
                                                points["F"] = o
                                                for p in values:
                                                    if p != y and p !=x and p != z and p != l and p !=m and p != o:
                                                        points["G"] = p
                                                        for q in values:
                                                            if q != y and q !=x and q != z and q != l and q !=m and q != o and q !=p:
                                                                points["H"] = q
                                                                for r in values:
                                                                    if r != y and r !=x and r != z and r != l and r !=m and r != o and r !=p and r != q:
                                                                        points["I"] = r
                                                                        for a in points:
                                                                            if (points[a] == len1) or (points[a] == len2) or (points[a] == len3) or (points[a] == len4) or (points[a] == len5) or (points[a] == len6) or (points[a] == len7) or (points[a] == len8):
                                                                                points[a] = 11
                                                                        if ((points["A"] < points["E"]) and (points["A"] + 1 == points["I"] or points["A"] - 1 == points["I"])) or ((points["A"] < points["D"]) and (points["A"] + 1 == points["G"] or points["A"] - 1 == points["G"])) or ((points["A"] < points["B"]) and (points["A"] + 1 == points["C"] or points["A"] - 1 == points["C"])) or ((points["B"] < points["E"]) and (points["B"] + 1 == points["H"] or points["B"] - 1 == points["H"])) or ((points["C"] < points["E"]) and (points["C"] + 1 == points["G"] or points["C"] - 1 == points["G"])) or ((points["C"] < points["F"]) and (points["C"] + 1 == points["I"] or points["C"] - 1 == points["I"])) or ((points["D"] < points["E"]) and (points["D"] + 1 == points["F"] or points["D"] - 1 == points["F"])) or ((points["G"] < points["H"]) and (points["G"] + 1 == points["I"] or points["G"] - 1 == points["I"])):
                                                                            total_possibilities += 1
                                                                            incorrect_possibilities +=1
                                                                        
                                                                        else:
                                                                            correct_possibilities +=1
                                                                            total_possibilities +=1
                                                                              
def factorial(f):
    factor_count = 1
    multiplier = 1
    while factor_count < 9 - int(f):
        multiplier = multiplier * (factor_count + 1)
        factor_count += 1
    return multiplier

new_total_correct = correct_possibilities / factorial(chain_len)       
print ("%s Total Possibilities" %total_possibilities)
print ("%s Correct possibilities" %correct_possibilities)
print ("%s Incorrect possibilities" %incorrect_possibilities)
print ("%s New total correct" %new_total_correct)        









