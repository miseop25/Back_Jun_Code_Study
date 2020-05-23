import sys
input = sys.stdin.readline

if __name__ == "__main__":
    num = dict()
    for i in range(1,31):
        num[i] = 0
    for _ in range(28) :
        num[int(input())] = 1
    answer = sorted(num.items(), key= lambda x: x[1])
    print(answer[0][0])
    print(answer[1][0])
