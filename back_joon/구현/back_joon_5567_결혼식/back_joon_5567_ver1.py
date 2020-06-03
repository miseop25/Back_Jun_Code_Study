import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    m = int(input())
    answer = dict()
    friend = dict()

    for i in range(m) :
        a, b = map(int, input().split(" "))
        if a == 1 :
            if b not in answer :
                answer[b] = True
        else :
            if a in friend :
                friend[a].append(b)
            else :
                friend[a] = [b]
    midResult = list(answer.keys())
    for key in midResult :
        for i in friend[key] :
            if i == 1 : continue
            answer[i] = True
    
    print(len(answer))


