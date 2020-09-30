import sys
input = sys.stdin.readline 

def soluction(word) :
    notFox = set()
    while True :
        check = input().rstrip()
        if check == "what does the fox say?" :
            break
        temp = list(map(str, check.split(" ")))

        notFox.add(temp[-1])
    answer = []
    for i in word :
        if i not in notFox :
            answer.append(i)


    
    return ' '.join(answer)

if __name__ == "__main__":
    T = int(input())
    for _ in range(T) :
        word = list(map(str, input().rstrip().split(" ")))
        print(soluction(word))
