import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    answer = []
    for _ in range(N) :
        answer.append(int(input()))
    answer = sorted(answer)
    for i in answer :
        print(i)
