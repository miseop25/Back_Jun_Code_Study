import sys
input = sys.stdin.readline

if __name__ == "__main__":
    word = []
    for _ in range(5) :
        word.append(input().rstrip())
    
    answer = ''
    for i in range(15) :
        for j in range(5) :
            try :
                answer += word[j][i]
            except :
                pass
    print(answer)