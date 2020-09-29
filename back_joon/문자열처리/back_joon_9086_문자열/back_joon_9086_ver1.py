import sys
input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    for _ in range(T) :
        word = input().rstrip()
        answer = word[0] + word[-1]
        print(answer)