def soluction():
    word = (input().rstrip()).lower()
    cntDict = dict()
    for k in word :
        cntDict.setdefault(k, 0)
        cntDict[k] += 1
    result = list(sorted(cntDict.items(), key= lambda x: -x[1]))
    if len(result) < 2 :
        answer = result[0][0]
        return answer.upper()
    if result[0][1] == result[1][1] :
        return "?"
    else :
        answer = result[0][0]
        return answer.upper()


if __name__ == "__main__":
    print(soluction())

    