import sys
input = sys.stdin.readline

if __name__ == "__main__":
    plantDict = dict()
    total = 0
    while True :
        name = input().rstrip().lstrip()
        if name == "" : break
        total += 1
        if name in plantDict :
            plantDict[name] += 1
        else :
            plantDict[name] = 1
    
    result = list(sorted(plantDict.items(), key= lambda x: x[0]))
    for i in result :
        per = (i[1]/total)*100
        print("%s %.4f"%(i[0], per))
        

