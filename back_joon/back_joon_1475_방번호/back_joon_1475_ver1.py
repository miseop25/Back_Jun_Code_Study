import math
N = str(input())

num_dict = dict()
for i in range(9) :
    num_dict[str(i)] = 0

for i in N :
    if i == "9" or i == "6" : 
        num_dict["6"] += 1
    else :
        num_dict[i] += 1

if num_dict["6"] > 0 :
    num_dict["6"] = math.ceil(num_dict["6"]/2)
print(max(num_dict.values()))

