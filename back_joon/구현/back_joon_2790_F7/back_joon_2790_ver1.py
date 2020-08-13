import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    score = []
    for _ in range(N) :
        score.append(int(input()))
    score = sorted(score, reverse= True)
    answer = 1
    comp = score[0] + 1
    for i in range(1, N) :
        if comp <= score[i] + N :
            answer += 1
            comp = max(comp, score[i]+i)
        else :
            break
    print(answer)