abc = list(map(int, input().split(" ")))
temp = input().rstrip()
alpa_dict = dict()
abc = sorted(abc, key= lambda x: x)
alpa_dict["A"] = abc[0]
alpa_dict["B"] = abc[1]
alpa_dict["C"] = abc[2]

answer = []
for i in temp :
    answer.append(str(alpa_dict[i]))
print(" ".join(answer))
