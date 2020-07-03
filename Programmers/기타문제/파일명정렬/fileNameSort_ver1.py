def splitFile(f) :
    head = ''
    number = ''
    flag = True
    for i in range(len(f)) :
        if f[i] >= "0" and f[i] <= "9" :
            number += f[i]
            flag = False
        else :
            if not flag :
                flag = True
                break
    if flag :
        head = f[: i - len(number)]
    else :
        head = f[: -len(number)]
    return head.lower(), int(number)


        
def solution(files):
    answer = []
    fDict = dict()
    for i, name in enumerate(files) :
        head, num = splitFile(name)
        fDict[name] = [head, num,  i]
    result = sorted(fDict.items(), key= lambda x: (x[1][0], x[1][1], x[1][2]))
    for i in result :
        answer.append(i[0])
    return answer

# print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["abs00", "abs123"]))