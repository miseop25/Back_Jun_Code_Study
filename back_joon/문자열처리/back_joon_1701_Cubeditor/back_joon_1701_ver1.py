if __name__ == "__main__":
    s = input().rstrip()
    wordDict = dict()

    for i in range(len(s) - 1) :
        for j in range(1, len(s[i:])//2 ) :
            temp = s[i: i+j] 
            cnt = s.count(temp)
            if cnt < 2 : continue
            if temp in wordDict :
                continue
            wordDict[temp] = cnt
    result = sorted(wordDict.items(), key= lambda x: -len(x[0]))
    for a in result :
        if a[1] != 1 :
            print(len(a[0]))
            break

