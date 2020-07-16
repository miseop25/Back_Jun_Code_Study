def makeSplitList(l) :
    result = []
    val = l - 2
    for v in range(val, 0, -1) :
        a = (l-v)//2
        b = (l-v) - a
        if a == b and v == a :
            result.append([a,a,a])
            continue

        c1 = [a, b, v]
        c2 = [a, v, b]
        c3 = [v, a, b]
        result.append(c1)
        result.append(c2)
        result.append(c3)
        if a != b :
            c4 = [b, v, a]
            c5 = [v, b, a]
            c6 = [b, a, v]
            result.append(c4)
            result.append(c5)
            result.append(c6)
    return result

def changeWord(ar, w) :
    a = w[:ar[0]] 
    b = w[ar[0]:ar[1]+ar[0]]
    c = w[ar[1]+ar[0]:]
    result = a[::-1] + b[::-1] + c[::-1]
    return result


def soluction() :
    word = input().rstrip()
    answer = set()
    l = len(word)
    splList = makeSplitList(l)
    for s in splList :
        answer.add(changeWord(s, word))
    result = list(sorted(answer)) 
    return result[0]


if __name__ == "__main__":
    print(soluction())
    